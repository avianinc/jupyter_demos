// fetch arguments
args=sciargs();
Amp = strtod(args(3)); 
Freq = strtod(args(4)); 

//Amp = 1; 
//Freq = 3; 

// load the blocks library and the simulation engine
//loadXcosLibs();
loadScicos();

importXcosDiagram("/root/jupyter_demos/API_Demo/models/scilab_sine.zcos")

typeof(scs_m) //The diagram data structure

//This diagram uses 3 context variables : 
//  Amplitude : the sin function amplitude
//  Pulsation : the sin function pulsation
//  Tf        : the final simulation time
scs_m.props.context; //the embedded definition

// Simulate the model
Context.Amp=Amp;
Context.Freq=Freq;
scicos_simulate(scs_m,list(),Context,'nw');

// Output response
disp(A.values);

// exit
exit;