function BW = setTr(imgName, val)
    img = pgmread(imgName);
    BW = imbinarize(img, val);
    my_disp(BW);
end