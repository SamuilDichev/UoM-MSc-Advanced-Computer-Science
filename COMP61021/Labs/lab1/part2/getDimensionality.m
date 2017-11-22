function [k, PoV, E] = getDimensionality(V)
    SV = sum(V);
    
    for k = 1: size(V, 1);
       PoV = sum(V(1:k, 1)) / SV;
       E = SV - sum(V(1:k, 1));
       if PoV >= 0.9
           break
       end
    end
end