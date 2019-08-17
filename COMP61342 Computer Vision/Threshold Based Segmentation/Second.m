tray = pgmread('tray.pgm');
filTray = imgaussfilt(tray, 25);
newTray = imsubtract(tray, filTray);

my_disp(newTray);
% Y = roihist();


k = 10;
sigma1 =  0.5;
sigma2 = sigma1*k;

hsize = [3, 3];
h1 = fspecial('gaussian', hsize, sigma1);
h2 = fspecial('gaussian', hsize, sigma2);
gauss1 = imfilter(newTray, h1, 'replicate');
gauss2 = imfilter(newTray, h2, 'replicate');
dogImg = gauss1 - gauss2;

testTray = imsubtract(newTray, dogImg);

% pause(5);
BWF1 = imbinarize(newTray, -35);
BWF2 = imbinarize(testTray, -30);
% BWF = imbinarize(newTray,'adaptive','ForegroundPolarity','dark','Sensitivity', 0.5);
%my_disp(BWF);
imshowpair(BWF1, BWF2, 'montage')