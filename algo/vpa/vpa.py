// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © karthikmarar

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © karthikmarar

//@version=4
study("VPA ANALYSIS ", overlay=true)
trind = input(title="Trend Indication", type=input.bool, defval=false)
bkbg  = input(title="Black Background", type=input.bool, defval=false)
plot50 = input(title="Plot 50 MA", type=input.bool, defval=false)
plot200 = input(title="Plot 200 MA", type=input.bool, defval=false)
plot(plot50? sma(close,50): na, color= color.blue, style = plot.style_line )
plot(plot200? sma(close,200): na, color= color.red, style = plot.style_line )
//===================== Basic Definitions =======================================

volAvg = sma(volume,40)
volMean = stdev(volAvg,30)
volUpBand3 = volAvg + (3*volMean)
volUpBand2 = volAvg + (2*volMean)
volUpBand1 = volAvg + (1*volMean)
volDnBand1 = volAvg -(1*volMean)
volDnBand2 = volAvg - (2*volMean)
H = high
L = low
V = volume
C = close
midprice = (H+L)/2
spread = (H-L)
avgSpread = sma(spread,40)
AvgSpreadBar        =   spread > avgSpread// to be checked
wideRangeBar = spread>(1.5*avgSpread)
narrowRangeBar   = spread<(0.7*avgSpread)
lowVolume = V<volume[1] and V<volume[2] and V <volAvg // mods
upBar       = C>close[1]//C>Ref(C,-1)
downBar     = C<close[1]//C<Ref(C,-1)
highVolume  = V>volume[1] and volume[1]>volume[2]// Review
closeFactor = C-L
clsPosition = spread/closeFactor
closePosition       = ((closeFactor == 0) ? (avgSpread) : (clsPosition))
vb          = V > volAvg or V> volume[1]          
upClose     = C>=((spread*0.7)+L)// close is above 70% of the Bar
downClose   = C<=((spread*0.3)+L)// close is below the 30% of the bar
aboveClose  = C>((spread*0.5)+L)// close is between 50% and 70% of the bar
belowClose  = C<((spread*0.5)+L)// close is between 50% and 30% of the bar
midClose    = C>((spread*0.3)+L) and C<((spread*0.7)+L)// close is between 30% and 70% of the bar
veryLowClose  = closePosition>4//close is below 25% of the bar
veryHighClose = closePosition<1.35// Close is above 80% of the bar


ClosePos = iff(C<=((spread*0.2)+L),1,iff(C<=((spread*0.4)+L),2,iff(C<=((spread*0.6)+L),3,iff(C<=((spread*0.8)+L),4,5))))
//1 = downClose, 2 = belowClose, 3 = midClose, 4 = aboveClose, 6 = upClose
volpos =   iff(V>(volAvg*2),1,iff(V>(volAvg*1.3),2,iff(V>volAvg,3,iff(V<volAvg and (V<volAvg*0.7) ,4,5))))
//1 = veryhigh, 2 = High , 3 = AboveAverage, 4  = volAvg //LessthanAverage, 5 = lowVolume

freshGndHi   = high == highest(high,5)?1:0
freshGndLo   = low  == lowest(low,5)?1:0
//=========================================================================|
//                    Trend Analysis Module                                | 
//=========================================================================|

psmin = input(2,"Short term Min periods", input.integer, minval=1, maxval=9, step=1)  
psmax = input(8,"Short term Max Periods", input.integer, minval=1, maxval=9, step=1)

rshmin = (high - nz(low[psmin])) / (atr(psmin) * sqrt(psmin))
rshmax = (high - nz(low[psmax])) / (atr(psmax) * sqrt(psmax))
RWIHi  = max(rshmin,rshmax)

rslmin = (nz(high[psmin]) - low) / (atr(psmin) * sqrt(psmin))
rslmax = (nz(high[psmax]) - low) / (atr(psmax) * sqrt(psmax))
RWILo  = max(rslmin,rslmax)

k      = RWIHi-RWILo
ground = RWIHi  
sky    = RWILo  

plmin = input(10,"Long Term Min Periods", type=input.integer, minval=1, maxval=32, step=1) 
plmax = input(40,"Long term Max Periods", type=input.integer, minval=1, maxval=64, step=1) 

rlhmin = (high - nz(low[plmin])) / (atr(plmin) * sqrt(plmin))
rlhmax = (high - nz(low[plmax])) / (atr(plmax) * sqrt(plmax))
RWILHi  = max(rlhmin,rlhmax)

rllmin = (nz(high[plmin]) - low) / (atr(plmin) * sqrt(plmin))
rllmax = (nz(high[plmax]) - low) / (atr(plmax) * sqrt(plmax))
RWILLo  = max(rllmin,rllmax)

j      = RWILHi-RWILLo
j2     = RWILHi 
k2     = RWILLo 

ja     = crossover(j,1) // The following section check the diffeent condition of the RWi above and below zero
jb     = crossover(1,j) // In oder to check which trend is doing what
jc     = crossover(-1,j)
jd     = crossover(j,-1)
j2a    = crossover(j2,1)
j2b    = crossover(1,j2)
k2a    = crossover(k2,1)
k2b    = crossover(1,k2)
//Define the Major, Minor and Immediate trend Status
upmajoron   = j > 1 and ja[1]
upmajoroff  = j < 1 and jb[1]
upminoron   = j2 > 1 and j2a[1]
upminoroff  = j2 < 1 and j2b[1]
dnmajoron   = j < -1 and jc[1]
dnmajoroff  = j > -1 and jd[1]
dnminoron   = k2 > 1 and k2a[1]
dnminoroff  = k2 < 1 and k2b[1]
upmid       = iff(ground > 1, 1,0)
dnimd       = iff(sky > 1, 1, 0)
upmajor     = iff(j>1,1,iff(j<(-1),-1,0))
upminor     = iff(j2>1,1,-1)
dnminor     = iff(k2>1,1,-1)

plotshape(upmajor ==1 and trind == true , text="",style=shape.triangledown, color= color.lime, location=location.top,transp=0, size= size.small)
plotshape(upmajor == -1 and trind == true , text="",style=shape.triangledown, color=color.red, location=location.top,transp=0, size = size.small)
plotshape(upmajor != -1 and upmajor != 1 and trind == true , text="",style=shape.triangledown, color=color.yellow, location=location.top,transp=0, size = size.small)

plotshape(upmid ==1 and trind == true  , text="",style=shape.circle, color= color.lime, location=location.top,transp=0,size = size.tiny)
plotshape(upmid == -1 and trind == true , text="",style=shape.circle, color= color.red, location=location.top,transp=0,size = size.tiny)
plotshape(upmid != -1 and upmid !=1 and trind == true , text="",style=shape.circle, color= color.yellow, location=location.top,transp=0,size = size.tiny)

plotshape(upminor == 1 and trind == true , text="",style=shape.square, color= color.lime, location=location.top,transp=0 )
plotshape(upminor == -1 and trind == true , text="",style=shape.square, color= color.red, location=location.top,transp=0)
plotshape(upminor != 1 and upminor != -1 and trind == true , text="",style=shape.square, color= color.yellow, location=location.top,transp=0)
//=========================================================================|
//                    Slope Calculation                                    |
//=========================================================================|
src = sma(close,5)
//--------------longterm trend---------------
lts      = linreg(src, 40, 0)
ltsprev  = linreg(close[3], 40, 0)
ltsslope = ((lts - ltsprev) / 3 )
//-------------Medium Term Trend-------------
mts      = linreg(src, 20, 0)
mtsprev  = linreg(close[3], 20, 0)
mtsslope = ((mts - mtsprev) / 3 )
//-------------short Term Trend-------------
sts      = linreg(src, 3, 0)
stsprev  = linreg(close[1], 3, 0)
stsslope = ((sts - stsprev) / 2 )
tls      = stsslope
//=========================================================================|
//                    VSA SIGNAL GENERATION                                |
//=========================================================================|
upThrustBar  = wideRangeBar and downClose  and high > high[1] and upmid==1 //WRB and UHS in midterm trend
nut          = wideRangeBar and downClose  and freshGndHi and highVolume   // NEW SIGNAL - Upthrust after new short up move
bc           = wideRangeBar and aboveClose and volume == highest(volume,60) and upmajor==1 // Buying Climax
upThrustBar1 = wideRangeBar and (ClosePos==1 or ClosePos==2) and upminor>0 and H>H[1]and (upmid>0 or upmajor>0) and volpos < 4 // after minor up trend

upThrustBartrue = wideRangeBar and ClosePos==1 and upmajor>0 and H>H[1] and volpos < 4//occurs after a major uptrend
upThrustCond1   = upThrustBar[1] and downBar and not narrowRangeBar // The Bar after Upthrust Bar- Confirms weakness
upThrustCond2   = upThrustBar[1] and downBar and V>(volAvg*1.3) // The Bar after Upthrust Bar- Confirms weakness
upThrustCond3   = upThrustBar and V>(volAvg*2) // Review
topRevBar       = V[1]>volAvg  and upBar[1] and wideRangeBar[1] and downBar and downClose and wideRangeBar and upmajor>0 and H==highest(H,10)// Top Reversal bar
PseudoUpThrust  = (upBar[1])and H>H[1] and V[1]>1.5*volAvg and downBar and downClose and not upThrustBar
pseudoUtCond    = PseudoUpThrust[1] and downBar and downClose and not upThrustBar
trendChange     = upBar[1] and H==highest(H,5) and downBar and (downClose or midClose) and V>volAvg and upmajor>0 and upmid>0 and not wideRangeBar and not PseudoUpThrust
noDemandBarUt   = upBar and narrowRangeBar and lowVolume and (aboveClose or upClose) and ((upminor>=0 and upmid>=0) or (upminor<=0 and upminor>=0))//in a up market
noDemandBarDt   = upBar and narrowRangeBar and lowVolume and (aboveClose or upClose) and (upminor<=0 or upmid<=0)// in a down or sidewayss market
noSupplyBar     = downBar and narrowRangeBar and lowVolume  and midClose
             
lowVolTest      = low == lowest(low,5) and upClose and lowVolume
lowVolTest1     = low == lowest(low,5) and V<volAvg and L<L[1] and upClose and upminor>0 and upmajor>0
lowVolTest2     = lowVolTest[1]  and upBar and upClose

sellCond1       = (upThrustCond1 or upThrustCond2 or upThrustCond3)
sellCond2       = sellCond1[1]==0
sellCond        = sellCond1 and sellCond2
strengthDown0   = upmajor<0 and volpos < 4 and downBar[1] and upBar and ClosePos>3 and upminor <0 and upmid <=0
strengthDown    = volpos<4 and downBar[1] and upBar and ClosePos>3 and upmid<=00 and upminor<0                       // Strength after a down trend
strengthDown1   = upmajor<0 and V>(volAvg*1.5) and downBar[1] and upBar and  ClosePos>3 and upmid<=00 and upminor<0
strengthDown2   = upmid<=0 and V[1]<volAvg  and upBar and veryHighClose and volpos<4
buyCond1        = strengthDown or strengthDown1
buyCond         = upBar  and buyCond1[1]
stopVolume      = L==lowest(L,5)  and (upClose or midClose) and V>1.5*volAvg and upmajor<0
revUpThrust     = upBar and upClose and V>V[1] and V>volAvg and  wideRangeBar and downBar[1] and downClose[1] and upminor<0
effortUp        = H>H[1] and L>L[1] and C>C[1] and C>=((H-L)*0.7+L) and spread>avgSpread and volpos < 4 
effortUpfail    = effortUp[1] and (upThrustBar or upThrustCond1 or upThrustCond2 or upThrustCond3 or (downBar and AvgSpreadBar))
effortDown      = H<H[1] and L<L[1] and C<C[1] and C<=((H-L)*0.25+L) and wideRangeBar and V>V[1] 
effortDownFail  = effortDown[1] and ((upBar and AvgSpreadBar) or revUpThrust or buyCond1)
upflag          = (sellCond or buyCond or effortUp or effortUpfail or stopVolume or effortDown or effortDownFail or revUpThrust or noDemandBarDt or noDemandBarUt or noSupplyBar or lowVolTest or lowVolTest1 or lowVolTest2 or bc)
bullBar         = (V>volAvg or V>V[1]) and C<=((spread*0.2)+L) and upBar and not upflag
bearBar         = vb  and downClose and downBar and spread>avgSpread and not upflag


//=============================== PLOT SHAPES SECTION============================
//UPTHRUSTS


plotshape((upThrustBar or upThrustBartrue) and not effortUpfail and not sellCond and not bc, "UT1", style=shape.triangledown, location=location.abovebar, color=#990000, transp=0, text="UT1", textcolor=#990000, editable=false, size=size.tiny) 
UT1 = upThrustBar or upThrustBartrue
plotshape((upThrustCond1 or upThrustCond2 or nut) and not effortUpfail and not sellCond and not bc, "UT2", style=shape.triangledown, location=location.abovebar, color=#ff0000, transp=0, text="UT2", textcolor=#ff0000, editable=false, size=size.tiny) 
UT2 = upThrustCond1 or upThrustCond2
UT = UT1 or UT2
alertcondition(upThrustBar, title='Alert on UT1 an UT2 and UT', message='An Upthrust Bar. A sign of weakness. High Volume adds weakness.  A down bar after Upthrust adds weakness')

plotshape(topRevBar and not sellCond and not UT and not effortUpfail, "TRB", style=shape.triangledown, location=location.abovebar, color=#ff9900, transp=0, text="TRB", textcolor=#ff9900, editable=false, size=size.tiny) 
alertcondition(topRevBar   , title='Alert on TRB', message='Top Reversal. Sign of Weakness.  ')

plotshape(trendChange and not effortUpfail, "Tch", style=shape.triangledown, location=location.abovebar, color=#ff471a, transp=0, text="TC", textcolor=#ff471a, editable=false, size=size.tiny) 
alertcondition(trendChange  , title='Alert on TCH', message='High volume Downbar after an upmove on high volume indicates weakness.  ')

plotshape(PseudoUpThrust and not effortUpfail, "PUT", style=shape.triangledown, location=location.abovebar, color=#ff471a, transp=0, text="PUT", textcolor=#ff471a, editable=false, size=size.tiny) 
plotshape(pseudoUtCond and not effortUpfail, "PUC", style=shape.triangledown, location=location.abovebar, color=#ff471a, transp=0, text="PUC", textcolor=#ff471a, editable=false, size=size.tiny) 
alertcondition(PseudoUpThrust or pseudoUtCond  , title='Alert on PUT and PUC', message='Psuedo UpThrust.   A Sign of Weakness.A Down Bar closing down after a Pseudo Upthrust confirms weakness. ') 

plotshape(noDemandBarUt, "ND", style=shape.circle, location=location.abovebar, color=#ff471a, transp=0, text="ND", textcolor=#ff471a, editable=false, size=size.tiny) 
plotshape(noDemandBarDt, "ND", style=shape.circle, location=location.abovebar, color=#e6e600, transp=0, text="ND", textcolor=#ff471a, editable=false, size=size.tiny) 
alertcondition(noDemandBarUt or noDemandBarDt  , title='Alert on ND', message='No Demand in a Uptrend. A sign of Weakness. Otherwise upside unlikely soon ') 

plotshape(noSupplyBar, "NS", style=shape.circle, location=location.belowbar, color=color.lime, transp=0, text="NS", textcolor=color.green, editable=false, size=size.tiny) 
alertcondition(noSupplyBar , title='Alert on NS', message='No Supply. A sign of Strength.  ') 

plotshape(lowVolTest and not effortDownFail, "LVT", style=shape.circle, location=location.belowbar, color=color.lime, transp=0, text="LVT", textcolor=color.green, editable=false, size=size.tiny) 
plotshape(lowVolTest2 and not effortUp, "ST", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="ST", textcolor=color.green, editable=false, size=size.tiny) 
lvt = lowVolTest or lowVolTest2
alertcondition(lvt , title='Alert on LVT', message='Test for supply.An upBar closing near High after a Test confirms strength.  ') 
//-------------------------------------------------
EFD = effortDownFail
ST1 = strengthDown0
ST2 = strengthDown and not strengthDown2
strcond = (strengthDown2 and not strengthDown0 and not strengthDown and not strengthDown1)? 1:0
ST3 = strengthDown1
ST4 = strengthDown2 and strcond
ST5 = strengthDown2 and not strcond
ST  = ST1 or ST2 or ST3 or ST4 or ST5
plotshape(strengthDown0 and not EFD and not effortUp and not stopVolume, "ST1", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="ST1", textcolor=color.green, editable=false, size=size.tiny) 
plotshape(strengthDown and not strengthDown2 and not EFD and not effortUp and not stopVolume, "ST2", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="ST1", textcolor=color.green, editable=false, size=size.tiny) 
plotshape(strengthDown1 and not EFD and not effortUp and not stopVolume, "ST3", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="ST1", textcolor=color.green, editable=false, size=size.auto)
plotshape(strengthDown2 and strcond and not EFD and not effortUp and not stopVolume, "ST4", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="ST2", textcolor=color.green, editable=false, size=size.tiny) 
alertcondition(ST , title='Alert on ST1, ST2, ST3, ST4 and ST', message='Strength seen returning after a down trend.  ') 
//----------------------------------------------

//---------------------------------------------------

plotshape(stopVolume and not ST, "SV", style=shape.circle, location=location.belowbar, color=color.lime, transp=0, text="SV", textcolor=color.green, editable=false, size=size.auto) 
plotshape(stopVolume and ST, "SV", style=shape.circle, location=location.belowbar, color=color.lime, transp=0, text="ST\nSV", textcolor=color.green, editable=false, size=size.auto) 
alertcondition(stopVolume , title='Alert on SV', message='Stopping volume. Normally indicates end of bearishness is nearing.  ') 

plotshape(effortUp and not ST and not buyCond and not effortDownFail, "EU", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="EU", textcolor=color.green, editable=false, size=size.tiny) 
alertcondition(effortUp , title='Alert on EU', message='Effort to Move up. Bullish Sign  ') 
plotshape(effortUp and ST and not buyCond, "EU", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="ST\nEU", textcolor=color.green, editable=false, size=size.tiny) 

plotshape(effortUpfail and not UT, "EUF", style=shape.triangledown, location=location.abovebar, color=color.red, transp=0, text="EUF", textcolor=color.red, editable=false, size=size.tiny) 
alertcondition(effortUpfail , title='Alert on EUF', message='Effort to Move up Failed. Bearish sign  ') 

plotshape(effortDown and not effortUpfail, "ED", style=shape.triangledown, location=location.abovebar, color=color.red, transp=0, text="ED", textcolor=color.green, editable=false, size=size.tiny) 
alertcondition(effortDown , title='Alert on ED', message='Effort to Move Down. Bearish Sign  ') 

plotshape(effortDownFail and not ST, "EDF", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="EDF", textcolor=color.green, editable=false, size=size.tiny) 
alertcondition(effortDownFail , title='Alert on EDF', message='Effort to Down Failed. Bullish sign  ') 
plotshape(effortDownFail and ST, "EDF", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="ST\nEDF", textcolor=color.green, editable=false, size=size.tiny) 

plotshape(revUpThrust and not ST, "RUT", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="RUT", textcolor=color.green, editable=false, size=size.auto) 
alertcondition(revUpThrust , title='Alert on RUT', message='Reverse Up Thrust - Bullish   ') 

plotshape(buyCond and not ST and not effortUp and not lvt, "BYC1", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="BYC", textcolor=color.green, editable=false, size=size.tiny) 
alertcondition(buyCond , title='Alert on BYC', message='Strength Returns - Buy Condition exist   ') 
plotshape(buyCond and not ST and effortUp, "BYC2", style=shape.triangleup, location=location.belowbar, color=color.lime, transp=0, text="EU\nBYC", textcolor=color.green, editable=false, size=size.tiny)

plotshape(sellCond and not UT, "SEC", style=shape.triangledown, location=location.abovebar, color=color.red, transp=0, text="SEC", textcolor=color.red, editable=false, size=size.tiny) 
alertcondition(sellCond  , title='Alert on SEC', message='Weakness Returns - Sell Condition exist   ') 
plotshape(sellCond and UT, "SEC", style=shape.triangledown, location=location.abovebar, color=color.red, transp=0, text="UT\nSEC", textcolor=color.red, editable=false, size=size.tiny) 

plotshape(bc and not UT, "BC", style=shape.triangledown, location=location.abovebar, color=color.red, transp=0, text="BC", textcolor=color.red, editable=false, size=size.tiny) 
alertcondition(bc  , title='Alert on BC', message='Buying Climax - End of Current Up Trend   ') 
plotshape(bc and UT, "BC", style=shape.triangledown, location=location.abovebar, color=color.red, transp=0, text="UT\nBC", textcolor=color.red, editable=false, size=size.tiny) 

//-----------------------------Bar coloring  Code-------------------------------------------------

//Vlp=Param("Volume lookback period",150,20,300,10);
Vrg=sma(volume,30)// average volume
rg=(high-close)
arg=wma(rg,30)
Vh=volume>volume[1] and volume[1]>volume[2]
Cloc=close-low
x=(high-low)/Cloc
x1=Cloc==0?arg:x
Vb1 = volume >Vrg or volume > volume[1]
ucls=x1<2
dcls=x1>2
mcls=x1<2.2 and x1>1.8 
Vlcls=x1>4
Vhcls=x1<1.35
upbar = close > close[1]
dnbar   =  close < close[1]
CloseUp =  close > close[1]
CloseDn =  close < close[1]
VolUp   =  volume > volume[1]
VolDn   =  volume < volume[1]
bb1 = upbar and CloseUp and ucls and low > low[1]
bb2 = upbar and VolUp
bb3 = dnbar and CloseDn and VolDn
bb4 = dnbar and CloseDn and close > close[1]
db1 = dnbar and CloseDn and dcls
db2 = dnbar and VolUp  
db3 = upbar and CloseDn and VolUp
db4 = upbar and CloseDn and close<low[1] and dcls
db5 = upbar and CloseUp and ucls and low<low[1]
db6 = upbar and CloseUp and dcls
bb=(bb1 or bb2 or bb3 or bb4)
db=(db1 or db2 or db3 or db4 or db5 or db6)


//neucolor = bkbg == true ? color.white : color.blue
mcolor = bb and tls>0? color.green : (db and tls<0? color.red: (bkbg == true ? color.white : color.blue)) 
bgcolor( bkbg == true? color.black : color.white, transp=0,  editable = false) 
barcolor(color=mcolor)


