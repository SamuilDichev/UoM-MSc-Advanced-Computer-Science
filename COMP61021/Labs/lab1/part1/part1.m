load iris;
allPCs = pca1(X);
pcs = zeros(4, 2);

% Choose PCs
pcs(:, 1) = allPCs(:, 2);
pcs(:, 2) = allPCs(:, 3);
%pcs(:, 3) = allPCs(:, 3);

compressedX = ones(2, 150);
xmean = mean(X, 2);
for i = 1: size(X, 2);
    x = X(:, i);
    z = pcs' * ( x -  xmean );
    compressedX(:, i) = z;
end

scatter(compressedX(1, :), compressedX(2, :), 'b.');
% scatter3(compressedX(1, :), compressedX(2, :), compressedX(3, :), 'b.');
xlabel('PC2');
ylabel('PC3');
zlabel('PC3');