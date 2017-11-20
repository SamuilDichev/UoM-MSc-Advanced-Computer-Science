function newData = toCol(data)
    newData = [];
    for i = 1: size(data, 2);
        img = data{i};
        for row = 1: size(img, 1); 
            for col = 1: size(img, 2);
                newData((row - 1) * size(img, 2) + col, i) = img(row, col);
            end
        end
    end
end