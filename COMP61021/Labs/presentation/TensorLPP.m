function [U, V, eigvalue_U, eigvalue_V, posIdx, Y] = TensorLPP(X, W, options)
% TensorLPP: Tensor Locality Preserving Projections
%
%       [U, V, eigvalue_U, eigvalue_V, posIdx, Y] = TensorLPP(X, W, options)
% 
%             Input:
%               X       -  3-d data matrix. X(:,:,i) is the i-th data
%                          sample.
%               W       -  Affinity matrix. You can either call "constructW"
%                          to construct the W, or construct it by yourself.
%               options -  Struct value in Matlab. The fields in options
%                          that can be set:
%                            nRepeat     -   The repeat times of the
%                                            iterative procedure. Default
%                                            10
%
%             Output:
%               U, V      - Embedding functions, for a new data point
%                           (matrix) x,  y = U'*x*V will be the embedding
%                           result of x. You might need to resort each
%                           element in y based on the posIdx.
%              eigvalue_U
%              eigvalue_V - corresponding eigenvalue.
% 
%               Y         - The embedding results, Each row vector is a
%                           data point. The features in Y has been sorted
%                           that Y(:,i) will be important to Y(:,j) with
%                           respect to the objective function if i<j 
%
%               posIdx    - Resort idx. For a new data sample (matrix) x, 
%                           y = U'*x*V, y is still a matrix. 
%                           You should convert it to a vector by :
%                               y = reshape(y,size(U,2)*size(V,2),1)'
%                           and resort the features by:
%                               y = y(posIdx)
%                           
% 
%    Examples:
%
%       fea = rand(50,100);
%       options = [];
%       options.Metric = 'Euclidean';
%       options.NeighborMode = 'KNN';
%       options.k = 5;
%       options.WeightMode = 'HeatKernel';
%       options.t = 1;
%       W = constructW(fea,options);
%       options.PCARatio = 0.99
%       options.ReducedDim = 5;
%       fea = reshape(fea',10,10,50);
%       [U, V, eigvalue_U, eigvalue_V, posIdx, Y] = TensorLPP(fea, W, options);
%       
%       
%       fea = rand(50,100);
%       gnd = [ones(10,1);ones(15,1)*2;ones(10,1)*3;ones(15,1)*4];
%       options = [];
%       options.Metric = 'Euclidean';
%       options.NeighborMode = 'Supervised';
%       options.gnd = gnd;
%       options.bLDA = 1;
%       W = constructW(fea,options);      
%       options.PCARatio = 1;
%       options.ReducedDim = 5;
%       fea = reshape(fea',10,10,50);
%       [U, V, eigvalue_U, eigvalue_V, posIdx, Y] = TensorLPP(fea, W, options);
% 
% 
% See also constructW, LPP.


%Reference:
%
%   Xiaofei He, Deng Cai and Partha Niyogi, "Tensor Subspace Analysis".
%   Advances in Neural Information Processing Systems 18 (NIPS 2005),
%   Vancouver, Canada, 2005.   
%
%   Xiaofei He, Deng Cai, Haifeng Liu and Jiawei Han, "Image Clustering
%   with Tensor Representation". ACM Multimedia 2005 , Nov. 2005, Hilton,
%   Singapore.
%
%    Written by Deng Cai (dengcai@gmail.com), Feb/2005, Feb/2006


if (~exist('options','var'))
   options = [];
else
   if ~strcmpi(class(options),'struct') 
       error('parameter error!');
   end
end

if ~isfield(options,'nRepeat')
    nRepeat = 10;
else
    nRepeat = options.nRepeat; %
end


[nRow,nCol,nSmp] = size(X);
DataMean = mean(X,3);
for i=1:nSmp
    X(:,:,i) = X(:,:,i)-DataMean;
end


U = eye(nRow);
V = eye(nCol);


D = diag(sum(W));
[i_idx,j_idx,v_idx] = find(W);


for repeat = 1:nRepeat 
    U_old = U;
    V_old = V;
    
    VV_T = V*V';
    S_v = zeros(nRow,nRow);
    D_v = zeros(nRow,nRow);
    for i=1:nSmp
        D_v = D_v + D(i,i)*X(:,:,i)*VV_T*X(:,:,i)';
    end
    for idx=1:length(i_idx)
        S_v = S_v + v_idx(idx)*X(:,:,i_idx(idx))*VV_T*X(:,:,j_idx(idx))';
    end
    D_v = max(D_v,D_v');
    S_v = max(S_v,S_v');
    
    if rank(D_v) < nRow 
        error('D_v not full rank');
    end

    [U, eigvalue_U] = eig(S_v,D_v);
    eigvalue_U = diag(eigvalue_U);
    [junk, index] = sort(-eigvalue_U);
    U = U(:, index);
    eigvalue_U = eigvalue_U(index);
    
    for i = 1:size(U,2)
        U(:,i) = U(:,i)./norm(U(:,i));
    end
    
    UU_T = U*U';
    S_u = zeros(nCol,nCol);
    D_u = zeros(nCol,nCol);
    for i=1:nSmp
        D_u = D_u + D(i,i)*X(:,:,i)'*UU_T*X(:,:,i);    
    end
    for idx=1:length(i_idx)
        S_u = S_u + v_idx(idx)*X(:,:,i_idx(idx))'*UU_T*X(:,:,j_idx(idx));
    end
    D_u = max(D_u,D_u');
    S_u = max(S_u,S_u');
    
    if rank(D_u) < nCol 
        error('D_u not full rank');
    end
    
    [V, eigvalue_V] = eig(S_u,D_u);
    eigvalue_V = diag(eigvalue_V);
    [junk, index] = sort(-eigvalue_V);
    V = V(:, index);
    eigvalue_V = eigvalue_V(index);

    for i = 1:size(V,2)
        V(:,i) = V(:,i)./norm(V(:,i));
    end
end

nRow = size(U,2);
nCol = size(V,2);

Y = zeros(nRow,nCol,nSmp);
for i=1:nSmp
    Y(:,:,i) = U'*X(:,:,i)*V;
end
Y = reshape(Y,nRow*nCol,nSmp)';


[nSmp,nFea] = size(Y);

allone = ones(nSmp,1);
tmp1 = diag(D)'*Y;
DPrime = sum((Y'*D)'.*Y)-tmp1.*tmp1/sum(diag(D));
LPrime = sum((Y'*W)'.*Y)-tmp1.*tmp1/sum(diag(D));
DPrime(find(DPrime < 1e-14)) = 10000;

LaplacianScore = LPrime./DPrime;
[dump,posIdx] = sort(-LaplacianScore);

if nargout == 6
    Y = Y(:,posIdx);
end

    
