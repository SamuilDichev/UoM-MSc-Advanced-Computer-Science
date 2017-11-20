load digit;

imgDim = 28;

% Convert matrices into column vectors
X = [];
for i = 1: size(train, 2);
    img = train{i};
    for row = 1: size(img, 1); 
        for col = 1: size(img, 2);
            X((row - 1) * size(img, 2) + col, i) = img(row, col);
        end
    end
end
      
allPCs = pca1(X);
pcs = [];

% Choose PCs
for i = 1: 784;
    pcs(:, i) = allPCs(:, i);
end

cTrain = [];
xmean = mean(X, 2);
for i = 1: size(X, 2);
    x = X(:, i);
    z = pcs' * ( x -  xmean);
    cTrain(:, i) = z;
end

% Convert column vectors back into matrices
dTrain = {};
for i = 1: size(cTrain, 2);
    img = [];
        rx = xmean + pcs * cTrain(:, i);
        for row = 1: imgDim; 
            for col = 1: imgDim;
                img(row, col) = rx((row - 1) * 28 + col, 1);
            end
        end
    dTrain{1, i} = img; 
end
