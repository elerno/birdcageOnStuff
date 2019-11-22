
sr		= 96000	; sample rate
kr		= 9600	; control rate
ksmps	= 10	; sr/kr
nchnls	= 1	; # of channels
0dbfs	= 1.0




    instr 1

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 2

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 3

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 4

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 5

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 6

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 7

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 8

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 9

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 10

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 11

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 12

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 13

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 14

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 15

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 16

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 17

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 18

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 19

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 20

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 21

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 22

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 23

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 24

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 25

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 26

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 27

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 28

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 29

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 30

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 31

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 32

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 33

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 34

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 35

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 36

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 37

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 38

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 39

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 40

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 41

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 42

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 43

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 44

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 45

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 46

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 47

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 48

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 49

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 50

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 51

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin


    instr 52

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenv	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
asig	oscili 1, kfreqenv, 1, i1
if ir == 0 kgoto end
    out asig * ampdbfs(kampenv) * 0.06666667
end:
    endin
