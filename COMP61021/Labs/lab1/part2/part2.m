function [dX, V, nPCs, PoV, E] = part2(train, test, numPCs)
imgDim = 28;

% Convert matrices into column vectors
newTrain = [];
for i = 1: size(train, 2);
    img = train{i};
    for row = 1: size(img, 1); 
        for col = 1: size(img, 2);
            newTrain((row - 1) * size(img, 2) + col, i) = img(row, col);
        end
    end
end

% Get PCs of train data
[allPCs, V] = pca2(newTrain);

% Set X to test data
X = [];
for i = 1: size(test, 2);
    img = test{i};
    for row = 1: size(img, 1); 
        for col = 1: size(img, 2);
            X((row - 1) * size(img, 2) + col, i) = img(row, col);
        end
    end
end

% Choose # of PCs to use
[nPCs, PoV, E] = getDimensionality(V);
for i = 1: numPCs;
    pcs(:, i) = allPCs(:, i);
end

% cX - compressed X, i.e. compressed test data
cX = [];
xmean = mean(X, 2);
for i = 1: size(X, 2);
    x = X(:, i);
    z = pcs' * ( x -  xmean);
    cX(:, i) = z;
end

% Convert column vectors back into matrices
% dX - decompressed X, i.e. decompressed test data
dX = {};
for i = 1: size(cX, 2);
    img = [];

    % rx - reconstructed x
    rx = xmean + pcs * cX(:, i);
    for row = 1: imgDim; 
        for col = 1: imgDim;
            img(row, col) = rx((row - 1) * imgDim + col, 1);
        end
    end

    dX{1, i} = img; 
end

end