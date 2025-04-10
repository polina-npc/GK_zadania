var pyramidModel = {
    "vertexPositions": new Float32Array([
        -7.5, 0.0, -7.5, 
         7.5, 0.0, -7.5, 
         7.5, 0.0,  7.5, 
        -7.5, 0.0,  7.5, 
        
         0.0, 15.0, 0.0 
    ]),

    "vertexNormals": new Float32Array([
       
        0.0, -1.0, 0.0,
        0.0, -1.0, 0.0,
        0.0, -1.0, 0.0,
        0.0, -1.0, 0.0,
        
        0.0, 1.0, -1.0,
        1.0, 1.0, 0.0,
        0.0, 1.0, 1.0,
       -1.0, 1.0, 0.0
    ]),

    "vertexTextureCoords": new Float32Array([
        0.0, 0.0,
        1.0, 0.0,
        1.0, 1.0,
        0.0, 1.0,
        0.5, 0.5
    ]),

    "indices": new Uint16Array([
      
        0, 1, 2,
        0, 2, 3,
       
        0, 1, 4,
        1, 2, 4,
        2, 3, 4,
        3, 0, 4
    ])
};
