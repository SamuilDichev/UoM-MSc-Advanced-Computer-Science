function [eigvector, eigvalue, bSuccess, Y] = OLPP(X, W, options)
% OLPP: Orthogonal Locality Preserving Projections
%
%       [eigvector, eigvalue, bSuccess] = OLPP(X, W, options)
% 
%             Input:
%               X       - Data matrix. Each row vector of fea is a data point.
%               W       - Affinity matrix. You can either call "constructW"
%                         to construct the W, or construct it by yourself.
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
%                            bDisp        -  0 or 1. diagnostic information
%                                            display
%
%             Output:
%               eigvector - Each column is an embedding function, for a new
%                           data point (row vector) x,  y = x*eigvector
%                           will be the embedding result of x.
%               eigvalue  - The eigvalue of OLPP eigen-problem. sorted from
%                           smallest to largest. 
%               bSuccess  - 0 or 1. Indicates whether the OLPP calcuation
%                           is successful. (OLPP needs matrix inverse,
%                           which will lead to eigen-decompose a
%                           non-symmetrical matrix. The caculation precsion
%                           of malab sometimes will cause imaginary numbers
%                           in eigenvectors. It seems that the caculation
%                           precsion of matlab is a little bit random, you
%                           can try again if not successful. More robust
%                           and efficient algorithms are welcome!) 
%                           
%                           
% 
% 
%       [eigvector, eigvalue, bSuccess, Y] = OLPP(X, W, options) 		
%               
%               Y:  The embedding results, Each row vector is a data point.
%                   Y = X*eigvector
% 
%    Examples:
%
%       fea = rand(50,70);
%       options = [];
%       options.Metric = 'Euclidean';
%       options.NeighborMode = 'KNN';
%       options.k = 5;
%       options.WeightMode = 'HeatKernel';
%       options.t = 1;
%       W = constructW(fea,options);
%       options.PCARatio = 0.99
%       options.ReducedDim = 5;
%       [eigvector, eigvalue, Y] = OLPP(fea, W, options);
%       
%       
%       fea = rand(50,70);
%       gnd = [ones(10,1);ones(15,1)*2;ones(10,1)*3;ones(15,1)*4];
%       options = [];
%       options.Metric = 'Euclidean';
%       options.NeighborMode = 'Supervised';
%       options.gnd = gnd;
%       options.bLDA = 1;
%       W = constructW(fea,options);      
%       options.PCARatio = 1;
%       options.ReducedDim = 5;
%       [eigvector, eigvalue, Y] = OLPP(fea, W, options);
% 
%
% Note: After applying some simple algebra, the smallest eigenvalue problem:
%				X^T*L*X = \lemda X^T*D*X
%      is equivalent to the largest eigenvalue problem:
%				X^T*W*X = \beta X^T*D*X
%		where L=D-W;  \lemda= 1 - \beta.
% Thus, the smallest eigenvalue problem can be transformed to a largest 
% eigenvalue problem. Such tricks are adopted in this code for the 
% consideration of calculation precision of Matlab.
% 
% 
% See also constructW, pca, lpp.


%Reference:
%
%   Deng Cai and Xiaofei He, "Orthogonal Locality Preserving Indexing" 
%   The 28th Annual International ACM SIGIR Conference (SIGIR'2005),
%   Salvador, Brazil, Aug. 2005.
%
%   Deng Cai, Xiaofei He, Jiawei Han and Hong-Jiang Zhang, "Orthogonal
%   Laplacianfaces for Face Recognition". IEEE Transactions on Image
%   Processing, Accepted for publication.
% 
%    Written by Deng Cai (dengcai@gmail.com), August/2004, Feb/2006


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
    ReducedDim = nFea-1; 
else
    ReducedDim = options.ReducedDim; 
end

if ReducedDim > nFea
    ReducedDim = nFea-1; 
end

if ~isfield(options,'bDisp')
    options.bDisp = 1;
end

%================nFea < nsmp===================

D = diag(sum(W));
%L = D - W;
L = W;

DPrime = X'*D*X;
DPrime = (DPrime+DPrime')/2;
LPrime = X'*L*X;
LPrime = (LPrime+LPrime')/2;
    

invDPrime = inv(DPrime);

eyenFea = eye(nFea);
eigvector = [];
eigvalue = [];

Q = invDPrime*LPrime;

bSuccess = 1;
for i = 1:ReducedDim,
    
    try
        option = struct('disp',0);
        [eigVec, eigv] = eigs(Q,1,'lr',option);
    catch
        eigvector = [];
        eigvalue = [];
        Y = [];
        disp('Error!');
        bSuccess = 0;
        return;
    end
    
    if ~isreal(eigVec)
    	disp('Virtual part!');
        bSuccess = 0;
		break;
    end
    	
    if eigv < 1e-14
        break;
    end
    
	eigvector = [eigvector, eigVec];	
    eigvalue = [eigvalue;eigv];

    Q = (eyenFea-invDPrime*eigvector*inv(eigvector'*invDPrime*eigvector)*eigvector')*invDPrime*LPrime;
    if options.bDisp
        disp([num2str(i),' eigenvector calculated!']);
    end
end

eigvalue = ones(length(eigvalue),1) - eigvalue;

if bSuccess
    eigvector = eigvector_PCA*eigvector;
else
    if size(eigvector,1) == size(eigvector_PCA,2)
        eigvector = eigvector_PCA*eigvector;
    end
end

if nargout == 4
    Y = old_X * eigvector;
end

