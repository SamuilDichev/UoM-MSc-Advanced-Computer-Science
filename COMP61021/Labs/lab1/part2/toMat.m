function newData = toMat(data)
    imgDim = 28;
    newData = {};
    for i = 1: size(data, 2);
        img = [];
        for row = 1: 28; 
            for col = 1: 28;
                img(row, col) = data((row - 1) * imgDim + col, i);
            end
        end

        newData{1, i} = img; 
    end
end