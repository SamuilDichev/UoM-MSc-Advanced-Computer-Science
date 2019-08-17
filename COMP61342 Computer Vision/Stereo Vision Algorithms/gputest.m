left_image = gpuArray(imread('shaft3rec.l.pgm'));
right_image = gpuArray(imread('shaft3rec.r.pgm'));

% Find the edges ( like this for instance, but however you like)
% -------------------------------------------------------------
left_edge_image = edge(left_image,'Sobel');
right_edge_image = edge(right_image,'Sobel');
