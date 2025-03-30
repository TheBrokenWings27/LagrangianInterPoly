clc
clear 
close all

%testing my paper writing program
xi = [1, 2, 4];
yi = [3, 2, 4];
n = length (xi);
x = sym("x");

A = x*ones(n,n);
B = repmat(xi(:), 1, n);
%C = repmat(xi, n,1); was only used once, ask about this approuch
top = prod(tril(A-B, -1) +eye(n) + triu(A-B, 1));
bot = prod(repmat(xi, n,1)-B + eye(n));
Poly = sum(yi.* top ./bot);
Poly = simplify(Poly)