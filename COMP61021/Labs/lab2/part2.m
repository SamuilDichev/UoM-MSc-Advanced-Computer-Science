basePath = pwd;
imgPath = fullfile(pwd, 'Image\');

[imgs,training] = lab_featuresets(imgPath, -1);