function [eigvector, eigvalue, Y] = LDA(X,gnd)
% LDA: Linear discriminant analysis (Fisherfaces approach PCA+LDA)
%
%       [eigvector, eigvalue] = LDA(X, gnd)
%
%             Input:
%               X     - Data matrix. Each row vector of fea is a data point.
%               gnd   - Colunm vector of the label information for each
%                       data point. 
%
%             Output:
%               eigvector - Each column is an embedding function, for a new
%                           data point (row vector) x,  y = x*eigvector
%                           will be the embedding result of x.
%               eigvalue  - The eigvalue of LDA eigen-problem. 
% 
% 
%       [eigvector, eigvalue, Y] = LDA(X, gnd) 		
%               
%               Y:  The embedding results, Each row vector is a data point.
%                   Y = X*eigvector
%

%	Reference:
%   
%         P. N. Belhumeur, J. P. Hespanha, and D. J. Kriegman, “Eigenfaces
%         vs. fisherfaces: recognition using class specific linear
%         projection,” IEEE Transactions on Pattern Analysis and Machine
%         Intelligence, vol. 19, no. 7, pp. 711-720, July 1997.  
%
%    Written by Deng Cai (dengcai@gmail.com), April/2004, Feb/2006




old_X = X;

% ====== Initialization
[nSmp,nFea] = size(X);
classLabel = unique(gnd);
nClass = length(classLabel);

bPCA = 0;
if nFea > (nSmp - nClass)
    PCAoptions = [];
    PCAoptions.ReducedDim = nSmp - nClass;
    [eigvector_PCA, eigvalue_PCA, meanData, new_X] = PCA(X,PCAoptions);
    X = new_X;
    [nSmp,nFea] = size(X);
    bPCA = 1;
end


sampleMean = mean(X);

MMM = zeros(nFea, nFea);
for i = 1:nClass,
	index = find(gnd==classLabel(i));
	classMean = mean(X(index, :));
	MMM = MMM + length(index)*classMean'*classMean;
end
W = X'*X - MMM;
B = MMM - nSmp*sampleMean'*sampleMean;

W = (W + W')/2;
B = (B + B')/2;

option = struct('disp',0);
[eigvector, eigvalue] = eigs(B,W,nClass-1,'la',option);
eigvalue = diag(eigvalue);

for i = 1:size(eigvector,2)
    eigvector(:,i) = eigvector(:,i)./norm(eigvector(:,i));
end

if bPCA 
    eigvector =eigvector_PCA*eigvector;
end

if nargout == 3
   Y = old_X * eigvector;
end

