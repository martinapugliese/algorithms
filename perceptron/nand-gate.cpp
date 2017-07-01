/* A NAND GATE */


#include "main_header.h"
#include "classes.h"


int main() {

    /* Defs and initialisations */
    Neuron n;
    signed int * weights;
    int * inputs;

    weights = new int [N];
    inputs = new int [N];

    /* Setting the bias of the neuron */
    n.setBias(-3);

    inputs[0] = 1;
    inputs[1] = 1;

    weights[0] = - 2;
    weights[1] = - 2;

    cout << n.computeOutput(inputs, weights) << endl;

    return 0;
}
