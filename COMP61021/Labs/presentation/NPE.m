function [eigvector, eigvalue, Y] = NPE(X, M, options)
% NPE: Neighborhood Preserving Embedding
%
%       [eigvector, eigvalue] = NPE(X, M, options)
% 
%             Input:
%               X       - Data matrix. Each row vector of fea is a data point.
%               M       - You can either call "constructM"
%                         to construct the M, or construct it by yourself.
%               options - Struct value in Matlab. The fields in options
%                         that can be set:
%                            ReducedDim   -  The dimensionality of the
%                                            reduced subspace. If 0,
%                                            all the dimensions will be
%                                            kept. Default is 0.
%                            PCARatio     -  The percentage of principal
%                                            component kept in the PCA
%                                            step. The percentage is
%                                            calculated based on the
%                                            eigenvalue. Default is 1
%                                            (100%, all the non-zero
%                                            eigenvalues will be kept.
%             Output:
%               eigvector - Each column is an embedding function, for a new
%                           data point (row vector) x,  y = x*eigvector
%                           will be the embedding result of x.
%               eigvalue  - The eigvalue of LPP eigen-problem. sorted from
%                           smallest to largest. 
% 
% 
%       [eigvector, eigvalue, Y] = NPE(X, M, options) 		
%               
%               Y:  The embedding results, Each row vector is a data point.
%                   Y = X*eigvector
%
%
%    Examples:
%
%       fea = rand(50,70);
%       options = [];
%       options.NeighborMode = 'KNN';
%       options.k = 5;
%       M = constructM(fea,options);
%       options.PCARatio = 0.99
%       [eigvector, eigvalue, Y] = NPE(fea, M, options);
%       
%       
%       fea = rand(50,70);
%       gnd = [ones(10,1);ones(15,1)*2;ones(10,1)*3;ones(15,1)*4];
%       options = [];
%       options.NeighborMode = 'Supervised';
%       options.gnd = gnd;
%       options.k = 0;
%       M = constructM(fea,options);
%       options.PCARatio = 1;
%       [eigvector, eigvalue, Y] = NPE(fea, M, options);
% 
% 
% 
%
% See also constructM, pca.

%Reference:
%
%   Xiaofei He, Deng Cai, Shuicheng Yan, and Hong-Jiang
%   Zhang, "Neighborhood Preserving Embedding", Tenth IEEE International 
%   Conference on Computer Vision (ICCV'2005), 2005
%
%   Sam Roweis & Lawrence Saul. "Nonlinear dimensionality reduction by 
%   locally linear embedding", Science, v.290 no.5500 , Dec.22, 2000. 
%   pp.2323--2326.
%
%    Written by Deng Cai (dengcai@gmail.com), Jan/2005, Jan/2007



if (~exist('options','var'))
   options = [];
else
   if ~strcmpi(class(options),'struct') 
       error('parameter error!');
   end
end

if ~isfield(options,'PCARatio')
    [eigvector_PCA, eigvalue_PCA, meanData, new_X] = PCA(X);
else
    PCAoptions = [];
    PCAoptions.PCARatio = options.PCARatio;
    [eigvector_PCA, eigvalue_PCA, meanData, new_X] = PCA(X,PCAoptions);
end
    
old_X = X;
X = new_X;



[nSmp,nFea] = size(X);

if nFea > nSmp
    error('X is not of full rank in column!!');
end

if ~isfield(options,'ReducedDim')
    ReducedDim = nFea; 
else
    ReducedDim = options.ReducedDim; 
end

if ReducedDim > nFea
    ReducedDim = nFea; 
end

W = sparse(eye(size(M)) - M);

WPrime = X'*W*X;
DPrime = X'*X;

DPrime = max(DPrime,DPrime');
WPrime = max(WPrime,WPrime');


dimMatrix = size(DPrime,2);
if (dimMatrix > 1500) & (ReducedDim < dimMatrix/10) 
    disp('use eigs to speed up!');
    option = struct('disp',0);
    [eigvector, eigvalue] = eigs(WPrime,DPrime,ReducedDim,'la',option);
    eigvalue = diag(eigvalue);
else
    [eigvector, eigvalue] = eig(WPrime,DPrime);
    eigvalue = diag(eigvalue);

    [junk, index] = sort(-eigvalue);
    eigvalue = eigvalue(index);
    eigvector = eigvector(:,index);
end

eigIdx = find(abs(eigvalue) < 1e-10);
eigvalue (eigIdx) = [];
eigvector(:,eigIdx) = [];


eigvalue = ones(length(eigvalue),1) - eigvalue;


if ReducedDim < size(eigvector,2)
    eigvector = eigvector(:, 1:ReducedDim);
    eigvalue = eigvalue(1:ReducedDim);
end

for i = 1:size(eigvector,2)
    eigvector(:,i) = eigvector(:,i)./norm(eigvector(:,i));
end



eigvector =eigvector_PCA*eigvector;

if nargout == 3
    Y = old_X * eigvector;
end


