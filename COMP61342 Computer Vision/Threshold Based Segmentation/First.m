BW1 = setTr('brains.pgm', 180);
BW2 = setTr('brains.pgm', 181);
BW3 = setTr('brains.pgm', 182);
BW4 = setTr('brains.pgm', 183);
BW5 = setTr('brains.pgm', 184);
BW6 = setTr('brains.pgm', 185);
BW7 = setTr('brains.pgm', 186);
BW8 = setTr('brains.pgm', 187);
BW9 = setTr('brains.pgm', 188);
BW10 = setTr('brains.pgm', 189);
BW11 = setTr('brains.pgm', 190);


BWA = imlincomb(.1, BW1, .1, BW2, .1, BW3, .1, BW4, .1, BW5, .1, BW6, .1, BW7, .1, BW8, .1, BW9, .1, BW10);
my_disp(BWA);

J = morphoImg(BWA, 'square', 3);

BWF = imbinarize(J, 0.8);
my_disp(BWF);

