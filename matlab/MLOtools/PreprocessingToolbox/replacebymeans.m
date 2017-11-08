%
% REPLACEBYMEANS
% Identifies missing values in the supplied data matrix
% and replaces them by the mean of their column.
%


function replaced = replacebymeans( data )

% Can barely remember how this works.
% Coded Sept 2007

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MAKE THE REPLACEMENT MATRIX
% WHERE THE VALUE IS MISSING, THIS MATRIX HAS THE MEAN.
% WHERE THE VALUE IS NOT MISSING, THIS VALUE HAS A '1'
%  ...SO WHEN I MULTIPLY THEM, THEY GET INSERTED
%
replacements = double(isnan(data)) .* repmat( nanmean(data), size(data,1), 1);
replacements( find(replacements==0) ) = 1;

%TURN NANs INTO 1s (DEPENDENT ON PREVIOUS STEP)
data( find( isnan(data) ) ) = 1;

%REPLACE!
replaced = data.*replacements;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

