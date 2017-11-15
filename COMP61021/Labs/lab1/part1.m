load iris;
allPCs = pca1(X);
pcs = zeros(4, 2);
pcs(:, 1) = allPCs(:, 1);
pcs(:, 2) = allPCs(:, 2);

newX = ones(2, 150);
xmean = mean(X, 2);
for i = 1: size(X, 2);
    x = X(:, i);
    z = pcs' * ( x -  xmean);
    newX(:, i) = z;
end

scatter(newX(1, :), newX(2, :));