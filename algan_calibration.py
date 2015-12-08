from __future__ import print_function, unicode_literals, division


def flowcalc(gr, initial_percent, ga_flow, al_flow, tar):

    """Input args in the following order: UV-VIS growth rate,
    UV-VIS percent, ga_flow,al_flow, target percent"""

    # Calculates the individual growth rates for Al and GaN in AlGaN growth
    initial_percent = initial_percent/100
    al_rate = initial_percent * gr
    ga_rate = gr - al_rate

    # Calculate growth rate per sccm
    al_rate_per = al_rate / al_flow
    ga_rate_per = ga_rate / ga_flow

    # Set TMAl flow at 50 sccm (max) and calculate TMGa flow
    # for target %. If TMGa flow is greater than 50, set Ga flow
    # to 50 and calculate TMAl flow
    tar = tar/100
    al_final = 50.0
    al_final_rate = al_final * al_rate_per
    ga_final_rate = (al_final_rate - (tar*al_final_rate))/tar
    ga_final = ga_final_rate / ga_rate_per

    if ga_final < 50.0:
#        print("\nTMGa flow: %.2f " % ga_final)
#        print("TMAl flow: %.2f " % al_final)
        return ga_final, al_final
    if ga_final > 50.0:
        ga_final = 50.0
        ga_final_rate = ga_final * ga_rate_per
        al_final_rate = (tar * ga_final_rate)/(1-tar)
        al_final = al_final_rate / al_rate_per
 #       print("\nTMGa flow: %.2f " % ga_final)
 #       print("TMAl flow: %.2f " % al_final)
        return ga_final, al_final
if __name__ == "__main__":
    # User input of AlGaN growth rate obtained from k-space data, and
    # the percentage Al in AlGaN from UV-VIS measurement
    try:
        gr = float(input("Growth Rate (nm/s): "))
        initial_percent = float(input("UV-VIS Al%: "))
        ga_flow = float(input("Calibration TMGa Flow Rate (sccm): "))
        al_flow = float(input("Calibration TMAl Flow Rate (sccm): "))
        tar = float(input("Target Al%: "))
    except Exception as e:
        print(e)
    a,b = flowcalc(gr, initial_percent, ga_flow, al_flow, tar)
    print(a,b)
    
