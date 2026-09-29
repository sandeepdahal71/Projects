#include <assert.h>
#include "../src/elevator.h"
int main(){Elevator e;elevator_init(&e);assert(e.state==OFF);elevator_event(&e,POWER_ON);assert(e.state==FLOOR2);elevator_event(&e,CALL_4);assert(e.state==MOVING_UP);elevator_event(&e,CAB_4);assert(e.state==STOPPED);elevator_event(&e,TIMER);assert(e.state==DOOR_OPENING);}
