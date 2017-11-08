x1 = [2 3 5 6];
x2 = [2 4 4 6];
x3 = [4 6 2 4];

scatter(x1, x2, 'b');
covx1x2 = cov(x1, x2)

hold on;
scatter(x1, x3, 'r*');
covx1x3 = cov(x1, x3)

scatter(x2, x3, 'g+');
covx2x3 = cov(x2, x3)

hold off;

xlim([0 10]);
ylim([0 10]);