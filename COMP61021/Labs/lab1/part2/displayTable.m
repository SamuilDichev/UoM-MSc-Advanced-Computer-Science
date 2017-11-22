function table = displayTable(train, test)
    table = [];
    height = size(test{1}, 1);
    width = size(test{1}, 2);
    maxPCs = 47;
    
    for i = 1: size(test, 2);
        for j = 1: width
            table(1:height, (i-1)*28 + j) = test{i}(1:height, j);
        end
    end
    
    for k = 1: 47;
        dX = part2(train, test, k);
        for i = 1: size(test, 2);
            for j = 1: width
                table(height*k+1:height*(k+1), (i-1)*28 + j) = dX{i}(1:height, j);
            end
        end
    end
end
