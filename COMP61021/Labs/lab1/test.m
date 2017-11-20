load digit;
img = [1 2 3; 4 5 6; 7 8 9;];

v = zeros(9, 1);

for row = 1: size(img, 1); 
    for col = 1: size(img, 2);
        v((row -1) * size(img, 2) + col, 1) = img(row, col);
    end
end

newImg = [];
for row = 1: size(img, 1); 
    for col = 1: size(img, 2);
         newImg(row, col) = v((row -1) * size(img, 2) + col, 1);
    end
end