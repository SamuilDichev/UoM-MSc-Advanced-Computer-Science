% Exercise - http://syllabus.cs.manchester.ac.uk/pgt/COMP61021/exercise/ex0.pdf
% More info - https://pdfs.semanticscholar.org/1ea8/2cc13f6b7352943aba6c987e3895e5161b9b.pdf
% More info - https://math.stackexchange.com/questions/894378/volume-of-a-cube-and-a-ball-in-n-dimensions

R = 1;
r = R*2;
maxd = 10;
for n = 1:maxd
    NballV(n) = (pi^(n/2) / gamma(n/2 + 1)) * R^n;
    NcubeV(n) = r^n;
    ratios(n) = NballV(n) / NcubeV(n); 
end

plot(ratios, '-o');
grid on;
ylabel('Ratio between the V of Sphere (R=1) and V of Cube(r=R*2)');
xlabel('Dimensions');