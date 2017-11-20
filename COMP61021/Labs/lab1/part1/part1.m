load iris;
allPCs = pca1(X);
pcs = zeros(4, 2);

% Choose PCs
pcs(:, 1) = allPCs(:, 1);
pcs(:, 2) = allPCs(:, 2);

compressedX = ones(2, 150);
xmean = mean(X, 2);
for i = 1: size(X, 2);
    x = X(:, i);
    z = pcs' * ( x -  xmean);
    compressedX(:, i) = z;
end

scatter(compressedX(1, :), compressedX(2, :));

decompressedX = ones(2, 150);
for i = 1: size(compressedX, 2);
    rx = xmean + pcs * compressedX(:, i);
    decompressedX(:, i) = rx;
end