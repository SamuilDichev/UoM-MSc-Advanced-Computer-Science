function graphPoV(V)
    SV = sum(V);
    
    PoVs = [];
    for k = 1: 180;
       PoV = sum(V(1:k, 1)) / SV;
       PoVs(k) = PoV;
    end
    
    plot(PoVs);
    hold on;
    plot(47,PoVs(47),'r*')
end