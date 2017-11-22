function l = getEigenvalue(A, v)
    syms l;
    l = solve(A*v == l*v, l);
end