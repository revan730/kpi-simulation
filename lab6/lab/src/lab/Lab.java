/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab;
import PetriObj.PetriNet;
import PetriObj.ArcIn;
import PetriObj.ArcOut;
import PetriObj.PetriP;
import PetriObj.PetriT;
import PetriObj.ExceptionInvalidNetStructure;
import PetriObj.ExceptionInvalidTimeDelay;
import graphpresentation.RunPetriObjModel;
import java.util.ArrayList;
import PetriObj.PetriSim;

/**
 *
 * @author revan730
 */
public class Lab {
    
    public static PetriNet CreateSMO() throws ExceptionInvalidTimeDelay {
        ArrayList<PetriP> d_P = new ArrayList<>();
	ArrayList<PetriT> d_T = new ArrayList<>();
	ArrayList<ArcIn> d_In = new ArrayList<>();
	ArrayList<ArcOut> d_Out = new ArrayList<>();
	d_P.add(new PetriP("P1",0));
	d_P.add(new PetriP("P2",2));
	d_P.add(new PetriP("P3",0));
	d_T.add(new PetriT("T1",1,Double.MAX_VALUE));
	d_T.get(0).setDistribution("exp", d_T.get(0).getTimeServ());
	d_T.get(0).setParamDeviation(0.0);
	d_In.add(new ArcIn(d_P.get(0),d_T.get(0),1));
	d_In.add(new ArcIn(d_P.get(1),d_T.get(0),1));
	d_Out.add(new ArcOut(d_T.get(0),d_P.get(1),1));
	d_Out.add(new ArcOut(d_T.get(0),d_P.get(2),1));
	PetriNet d_Net = new PetriNet("SMOwithoutQueue",d_P,d_T,d_In,d_Out);
	PetriP.initNext();
	PetriT.initNext();
	ArcIn.initNext();
	ArcOut.initNext();

	return d_Net;
    }

    public static PetriNet CreateNet1() throws ExceptionInvalidNetStructure, ExceptionInvalidTimeDelay {
	ArrayList<PetriP> d_P = new ArrayList<>();
	ArrayList<PetriT> d_T = new ArrayList<>();
	ArrayList<ArcIn> d_In = new ArrayList<>();
	ArrayList<ArcOut> d_Out = new ArrayList<>();
	d_P.add(new PetriP("P1",1));
	d_P.add(new PetriP("P2",0));
	d_P.add(new PetriP("P3",1));
	d_P.add(new PetriP("P4",0));
	d_P.add(new PetriP("P5",0));
	d_P.add(new PetriP("P6",1));
	d_P.add(new PetriP("P7",0));
	d_P.add(new PetriP("P8",1));
	d_P.add(new PetriP("P9",0));
	d_P.add(new PetriP("P10",1));
	d_P.add(new PetriP("P11",0));
	d_P.add(new PetriP("P12",1));
	d_T.add(new PetriT("T1",1.0));
	d_T.get(0).setDistribution("exp", d_T.get(0).getTimeServ());
	d_T.get(0).setParamDeviation(0.0);
	d_T.add(new PetriT("T2",1.0));
	d_T.get(1).setDistribution("exp", d_T.get(1).getTimeServ());
	d_T.get(1).setParamDeviation(0.0);
	d_T.add(new PetriT("T3",1.0));
	d_T.get(2).setDistribution("exp", d_T.get(2).getTimeServ());
	d_T.get(2).setParamDeviation(0.0);
	d_T.add(new PetriT("T4",1.0));
	d_T.get(3).setDistribution("exp", d_T.get(3).getTimeServ());
	d_T.get(3).setParamDeviation(0.0);
	d_T.add(new PetriT("T5",1.0));
	d_T.get(4).setDistribution("exp", d_T.get(4).getTimeServ());
	d_T.get(4).setParamDeviation(0.0);
	d_T.add(new PetriT("T6",1.0));
	d_T.get(5).setDistribution("exp", d_T.get(5).getTimeServ());
	d_T.get(5).setParamDeviation(0.0);
	d_T.add(new PetriT("T7",1.0));
	d_T.get(6).setDistribution("exp", d_T.get(6).getTimeServ());
	d_T.get(6).setParamDeviation(0.0);
	d_T.add(new PetriT("T8",1.0));
	d_T.get(7).setDistribution("exp", d_T.get(7).getTimeServ());
	d_T.get(7).setParamDeviation(0.0);
	d_T.add(new PetriT("T9",1.0));
	d_T.get(8).setDistribution("exp", d_T.get(8).getTimeServ());
	d_T.get(8).setParamDeviation(0.0);
	d_T.add(new PetriT("T11",1.0));
	d_T.get(9).setDistribution("exp", d_T.get(9).getTimeServ());
	d_T.get(9).setParamDeviation(0.0);
	d_T.add(new PetriT("T12",1.0));
	d_T.get(10).setDistribution("exp", d_T.get(10).getTimeServ());
	d_T.get(10).setParamDeviation(0.0);
	d_In.add(new ArcIn(d_P.get(0),d_T.get(0),1));
	d_In.add(new ArcIn(d_P.get(2),d_T.get(2),1));
	d_In.add(new ArcIn(d_P.get(1),d_T.get(2),1));
	d_In.add(new ArcIn(d_P.get(1),d_T.get(1),1));
	d_In.add(new ArcIn(d_P.get(4),d_T.get(3),1));
	d_In.add(new ArcIn(d_P.get(4),d_T.get(4),1));
	d_In.add(new ArcIn(d_P.get(5),d_T.get(4),1));
	d_In.add(new ArcIn(d_P.get(6),d_T.get(5),1));
	d_In.add(new ArcIn(d_P.get(6),d_T.get(6),1));
	d_In.add(new ArcIn(d_P.get(7),d_T.get(6),1));
	d_In.add(new ArcIn(d_P.get(8),d_T.get(7),1));
	d_In.add(new ArcIn(d_P.get(8),d_T.get(8),1));
	d_In.add(new ArcIn(d_P.get(9),d_T.get(8),1));
	d_In.add(new ArcIn(d_P.get(10),d_T.get(9),1));
	d_In.add(new ArcIn(d_P.get(11),d_T.get(9),1));
	d_In.add(new ArcIn(d_P.get(10),d_T.get(10),1));
	d_Out.add(new ArcOut(d_T.get(0),d_P.get(0),1));
	d_Out.add(new ArcOut(d_T.get(0),d_P.get(1),1));
	d_Out.add(new ArcOut(d_T.get(2),d_P.get(2),1));
	d_Out.add(new ArcOut(d_T.get(2),d_P.get(3),1));
	d_Out.add(new ArcOut(d_T.get(1),d_P.get(4),1));
	d_Out.add(new ArcOut(d_T.get(4),d_P.get(5),1));
	d_Out.add(new ArcOut(d_T.get(4),d_P.get(3),1));
	d_Out.add(new ArcOut(d_T.get(3),d_P.get(6),1));
	d_Out.add(new ArcOut(d_T.get(6),d_P.get(7),1));
	d_Out.add(new ArcOut(d_T.get(6),d_P.get(3),1));
	d_Out.add(new ArcOut(d_T.get(5),d_P.get(8),1));
	d_Out.add(new ArcOut(d_T.get(8),d_P.get(9),1));
	d_Out.add(new ArcOut(d_T.get(8),d_P.get(3),1));
	d_Out.add(new ArcOut(d_T.get(7),d_P.get(10),1));
	d_Out.add(new ArcOut(d_T.get(9),d_P.get(11),1));
	d_Out.add(new ArcOut(d_T.get(9),d_P.get(3),1));
	d_Out.add(new ArcOut(d_T.get(10),d_P.get(1),1));
	PetriNet d_Net = new PetriNet("1.g.pns.pns",d_P,d_T,d_In,d_Out);
	PetriP.initNext();
	PetriT.initNext();
	ArcIn.initNext();
	ArcOut.initNext();

	return d_Net;
}

public static PetriNet CreateNet4() throws ExceptionInvalidNetStructure, ExceptionInvalidTimeDelay {
	ArrayList<PetriP> d_P = new ArrayList<>();
	ArrayList<PetriT> d_T = new ArrayList<>();
	ArrayList<ArcIn> d_In = new ArrayList<>();
	ArrayList<ArcOut> d_Out = new ArrayList<>();
	d_P.add(new PetriP("P1",1));
	d_P.add(new PetriP("P2",0));
	d_P.add(new PetriP("Failed to buy from stock",0));
	d_P.add(new PetriP("P4",0));
	d_P.add(new PetriP("Went to other market",0));
	d_P.add(new PetriP("P6",0));
	d_P.add(new PetriP("Bought",0));
	d_P.add(new PetriP("P8",1));
	d_P.add(new PetriP("P9",0));
	d_P.add(new PetriP("P10",0));
	d_P.add(new PetriP("P11",0));
	d_P.add(new PetriP("Stock",72));
	d_T.add(new PetriT("T1",0.2));
	d_T.get(0).setDistribution("exp", d_T.get(0).getTimeServ());
	d_T.get(0).setParamDeviation(0.0);
	d_T.add(new PetriT("T2",1.0));
	d_T.get(1).setDistribution("exp", d_T.get(1).getTimeServ());
	d_T.get(1).setParamDeviation(0.0);
	d_T.add(new PetriT("T3",1.0));
	d_T.get(2).setDistribution("exp", d_T.get(2).getTimeServ());
	d_T.get(2).setParamDeviation(0.0);
	d_T.get(2).setProbability(0.8);
	d_T.add(new PetriT("T4",1.0));
	d_T.get(3).setDistribution("exp", d_T.get(3).getTimeServ());
	d_T.get(3).setParamDeviation(0.0);
	d_T.get(3).setProbability(0.2);
	d_T.add(new PetriT("T5",0.0));
	d_T.add(new PetriT("T6",1.0));
	d_T.get(5).setDistribution("exp", d_T.get(5).getTimeServ());
	d_T.get(5).setParamDeviation(0.0);
	d_T.add(new PetriT("T7",1.0));
	d_T.get(6).setDistribution("exp", d_T.get(6).getTimeServ());
	d_T.get(6).setParamDeviation(0.0);
	d_T.add(new PetriT("T8",1.0));
	d_T.get(7).setDistribution("exp", d_T.get(7).getTimeServ());
	d_T.get(7).setParamDeviation(0.0);
	d_T.add(new PetriT("T9",1.0));
	d_T.get(8).setDistribution("exp", d_T.get(8).getTimeServ());
	d_T.get(8).setParamDeviation(0.0);
	d_T.add(new PetriT("T10",3.0));
	d_T.get(9).setDistribution("exp", d_T.get(9).getTimeServ());
	d_T.get(9).setParamDeviation(0.0);
	d_In.add(new ArcIn(d_P.get(0),d_T.get(0),1));
	d_In.add(new ArcIn(d_P.get(1),d_T.get(1),1));
	d_In.add(new ArcIn(d_P.get(3),d_T.get(2),1));
	d_In.add(new ArcIn(d_P.get(3),d_T.get(3),1));
	d_In.add(new ArcIn(d_P.get(5),d_T.get(4),1));
	d_In.add(new ArcIn(d_P.get(1),d_T.get(5),1));
	d_In.add(new ArcIn(d_P.get(7),d_T.get(6),1));
	d_In.add(new ArcIn(d_P.get(8),d_T.get(7),1));
	d_In.add(new ArcIn(d_P.get(8),d_T.get(8),1));
	d_In.add(new ArcIn(d_P.get(10),d_T.get(9),1));
	d_In.add(new ArcIn(d_P.get(11),d_T.get(4),1));
	d_In.add(new ArcIn(d_P.get(11),d_T.get(5),1));
	d_In.add(new ArcIn(d_P.get(11),d_T.get(7),19));
	d_In.get(12).setInf(true);
	d_Out.add(new ArcOut(d_T.get(0),d_P.get(0),1));
	d_Out.add(new ArcOut(d_T.get(0),d_P.get(1),1));
	d_Out.add(new ArcOut(d_T.get(1),d_P.get(2),1));
	d_Out.add(new ArcOut(d_T.get(1),d_P.get(3),1));
	d_Out.add(new ArcOut(d_T.get(2),d_P.get(4),1));
	d_Out.add(new ArcOut(d_T.get(3),d_P.get(5),1));
	d_Out.add(new ArcOut(d_T.get(4),d_P.get(6),1));
	d_Out.add(new ArcOut(d_T.get(5),d_P.get(6),1));
	d_Out.add(new ArcOut(d_T.get(6),d_P.get(7),1));
	d_Out.add(new ArcOut(d_T.get(6),d_P.get(8),1));
	d_Out.add(new ArcOut(d_T.get(7),d_P.get(9),1));
	d_Out.add(new ArcOut(d_T.get(8),d_P.get(10),1));
	d_Out.add(new ArcOut(d_T.get(9),d_P.get(11),1));
	PetriNet d_Net = new PetriNet("net4",d_P,d_T,d_In,d_Out);
	PetriP.initNext();
	PetriT.initNext();
	ArcIn.initNext();
	ArcOut.initNext();

	return d_Net;
}
    
public static PetriNet CreateNetServers() throws ExceptionInvalidNetStructure, ExceptionInvalidTimeDelay {
	ArrayList<PetriP> d_P = new ArrayList<>();
	ArrayList<PetriT> d_T = new ArrayList<>();
	ArrayList<ArcIn> d_In = new ArrayList<>();
	ArrayList<ArcOut> d_Out = new ArrayList<>();
	d_P.add(new PetriP("Creator",1));
	d_P.add(new PetriP("P2",0));
	d_P.add(new PetriP("P3",20));
	d_P.add(new PetriP("PrimaryFailures",0));
	d_P.add(new PetriP("P5",0));
	d_P.add(new PetriP("Success",0));
	d_P.add(new PetriP("P7",0));
	d_P.add(new PetriP("P8",50));
	d_P.add(new PetriP("SecondaryFailures",0));
	d_T.add(new PetriT("T1",2.0));
	d_T.get(0).setDistribution("exp", d_T.get(0).getTimeServ());
	d_T.get(0).setParamDeviation(0.0);
	d_T.add(new PetriT("T2",20.0));
	d_T.get(1).setDistribution("exp", d_T.get(1).getTimeServ());
	d_T.get(1).setParamDeviation(0.0);
	d_T.get(1).setPriority(1);
	d_T.add(new PetriT("T3",0.0));
	d_T.add(new PetriT("T4",0.0));
	d_T.get(3).setProbability(0.3);
	d_T.add(new PetriT("T5",0.0));
	d_T.get(4).setProbability(0.7);
	d_T.add(new PetriT("T6",10.0));
	d_T.get(5).setDistribution("exp", d_T.get(5).getTimeServ());
	d_T.get(5).setParamDeviation(0.0);
	d_T.get(5).setPriority(1);
	d_T.add(new PetriT("T7",0.0));
	d_In.add(new ArcIn(d_P.get(0),d_T.get(0),1));
	d_In.add(new ArcIn(d_P.get(1),d_T.get(1),1));
	d_In.add(new ArcIn(d_P.get(2),d_T.get(1),1));
	d_In.add(new ArcIn(d_P.get(1),d_T.get(2),1));
	d_In.add(new ArcIn(d_P.get(4),d_T.get(3),1));
	d_In.add(new ArcIn(d_P.get(4),d_T.get(4),1));
	d_In.add(new ArcIn(d_P.get(6),d_T.get(5),1));
	d_In.add(new ArcIn(d_P.get(7),d_T.get(5),1));
	d_In.add(new ArcIn(d_P.get(6),d_T.get(6),1));
	d_Out.add(new ArcOut(d_T.get(0),d_P.get(0),1));
	d_Out.add(new ArcOut(d_T.get(0),d_P.get(1),1));
	d_Out.add(new ArcOut(d_T.get(1),d_P.get(2),1));
	d_Out.add(new ArcOut(d_T.get(2),d_P.get(3),1));
	d_Out.add(new ArcOut(d_T.get(1),d_P.get(4),1));
	d_Out.add(new ArcOut(d_T.get(3),d_P.get(5),1));
	d_Out.add(new ArcOut(d_T.get(4),d_P.get(6),1));
	d_Out.add(new ArcOut(d_T.get(5),d_P.get(7),1));
	d_Out.add(new ArcOut(d_T.get(6),d_P.get(8),1));
	d_Out.add(new ArcOut(d_T.get(5),d_P.get(1),1));
	PetriNet d_Net = new PetriNet("netServers",d_P,d_T,d_In,d_Out);
	PetriP.initNext();
	PetriT.initNext();
	ArcIn.initNext();
	ArcOut.initNext();

	return d_Net;
}
    /**
     * @param args the command line arguments
     * @throws PetriObj.ExceptionInvalidNetStructure
     * @throws PetriObj.ExceptionInvalidTimeDelay
     */
    public static void main(String[] args) throws ExceptionInvalidNetStructure, ExceptionInvalidTimeDelay {
        // TODO code application logic here
        //PetriNet p1 = Lab.CreateNetServers();
        PetriNet p1 = Lab.CreateNet4();
        PetriSim ps = new PetriSim(p1);
        ArrayList<PetriSim> arr;
        arr = new ArrayList<>();
        arr.add(ps);
        RunPetriObjModel r = new RunPetriObjModel(arr);
        r.go(1000);
        System.out.println("Finished");
    }
    
}
