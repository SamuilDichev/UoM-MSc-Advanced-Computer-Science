function J = morphoImg(img, SEshape, SEsize)
    se = strel(SEshape, SEsize);
    J = imopen(img, se);
    my_disp(J);
end