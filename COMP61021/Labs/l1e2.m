% Col Vectors
A = [3; 5; 2;];
B = [2; 1; 3;];

% Row Vectors
C = [2 4 6];
D = [1 3 2];

% Matrices
M1 = [1 2 3; 3 4 2; 2 7 3;];
M2 = [7 3 1; 9 7 4; 6 1 9;];

% Inner (dor) product works with any 2 vectors of same length.
% Doesn't matter if it's Col or Row vector
% Doesn't matter if the order of the vectors is reversed
innerproduct = dot(A, B);
innerproduct2 = dot(C, D);
innerproduct3 = dot(A, C);

% Does not work with 1 col and 1 row vector. Must be same types and sizes.
outerproduct = A.'*B;
outerproduct2 = C.'*D;

% Must be Square, i.e. same col / rows
determinantOfSquareMatrix = det(M1);
inverseOfSquareMatrix = inv(M1);
traceOfSquareMatrix = trace(M1);

% linearTransformation = 

eigenvaluesOfSquareMatrix = eig(M1);
[V, D] = eig(M1, M2);

covarianceOfVector = cov(A);