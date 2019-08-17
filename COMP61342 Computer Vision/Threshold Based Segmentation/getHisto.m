function Y = getHisto(imgName)
    img = pgmread(imgName);
    my_disp(img);
    Y = roihist();
end