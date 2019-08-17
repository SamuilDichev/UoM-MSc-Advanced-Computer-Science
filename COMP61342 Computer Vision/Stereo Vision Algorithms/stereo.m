% stereo.m
% A simple script for stereo
% 
% G.J. Edwards   gje@sv1.smb.man.ac.uk
%
% Notes for NAT/CJT..... I could make this considerably quicker by vectorizing
% 			the matching completely, but it would be for 
%			a beginner to understand.
% 			 You can ignore any concatenation warnings  
%			it's just warning you about concatenating
% 			empty vectors.
%			 I could probably fix it, but anyway.

% Load your images here, I've just generated some random data
% -----------------------------------------------------------
left_image = imread('shaft3rec.l.pgm');
right_image = imread('shaft3rec.r.pgm');

% Find the edges ( like this for instance, but however you like)
% -------------------------------------------------------------
left_edge_image = edge(left_image,'approxcanny', 0.25);
right_edge_image = edge(right_image,'approxcanny', 0.24);

% Display everything
% ------------------
figure(1);
subplot(2,2,1);
imagesc(left_image);
axis image, axis off, colormap gray;
title('Left Image');
subplot(2,2,2);
imagesc(right_image);
axis image, axis off, colormap gray;
title('Right Image');

subplot(2,2,3);
imagesc(left_edge_image);
axis image, axis off, colormap gray;
title('Left Edge Image');
subplot(2,2,4);
imagesc(right_edge_image);
axis image, axis off, colormap gray;
title('Right Edge Image');


% Now do the matching ( a basic understanding of Matlab is needed here )
% -----------------------------------------------------------------------
num_rows = size(left_image,1);
num_cols = size(right_image,2);
array_of_disparities = [];

for r = 1:num_rows
	left_edge_pixels = find(left_edge_image(r,:));
	for i = left_edge_pixels
		i1 = find(right_edge_image(r,:));
		disparities = (i1 - i)';
		num_matches = size(disparities,1);
		left_coords = repmat([i,r],num_matches,1);
		array_of_disparities = [array_of_disparities; [left_coords, disparities] ]; 
	end
end

% Focal Length
f_mm = 17;
px_size_mm = 0.011;
f_px = f_mm / px_size_mm;

% vars
Xs = [];
Ys = [];
Zs = [];
k = 1000000;
b = 0;

for i = 1:size(array_of_disparities, 1)
    xl = array_of_disparities(i, 1);
    yl = array_of_disparities(i, 2);
    Z = 1 / (k + array_of_disparities(i, 3) * px_size_mm);
    X = Z * ( xl / f_mm) - ( b / 2 );
    Y = Z * ( yl / f_mm);
    
    Zs = [Zs; Z];
    Xs = [Xs; X];
    Ys = [Ys; Y];
end

maxZ = max(Zs(:));
minZ = min(Zs(:));

maxX = max(Xs(:));
minX = min(Xs(:));

maxY = max(Ys(:));
minY = min(Ys(:));

Zscaled = (Zs - minZ) / (maxZ - minZ);
Xscaled = (Xs - minX) / (maxX - minX);
Yscaled = (Ys - minY) / (maxY - minY);

clf;
scatter(Xscaled, Zscaled, 1, '.');
% scatter(Xscaled, Zscaled, 1, '.');
% scatter3(Xscaled, Yscaled, Zscaled, 1, '.');
% set(gca,'Xdir','reverse')
title({'Graph of reconstructed image viewed from the above (X, Z)', 'Disparity and focal length in millimetres, k = 10000, Approxcanny'});
xlabel('X') % x-axis label
ylabel('Z') % y-axis label


% Display the table of candidate matches
% --------------------------------------
array_of_disparities;

