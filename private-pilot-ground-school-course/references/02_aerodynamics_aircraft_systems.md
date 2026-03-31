# Aerodynamics and Aircraft Systems

## Introduction

Understanding aerodynamics and aircraft systems is fundamental to safe flight operations. This guide covers the principles of flight, aircraft performance, and the major systems that make flight possible.

## Principles of Flight

### The Four Forces

**Lift**: Upward force created by airflow over wings
**Weight**: Downward force due to gravity
**Thrust**: Forward force from propeller/engine
**Drag**: Rearward force resisting motion

**Steady-State Flight**: Four forces in equilibrium
- Lift = Weight
- Thrust = Drag

### Bernoulli's Principle and Lift Generation

**Bernoulli's Principle**: As air velocity increases, pressure decreases

**Airfoil Design**:
- Curved upper surface (camber)
- Air travels faster over top
- Lower pressure above wing
- Higher pressure below wing
- Net upward force = Lift

**Angle of Attack (AOA)**: Angle between chord line and relative wind
- Increasing AOA increases lift (up to critical AOA)
- Beyond critical AOA: stall occurs

**Lift Equation**:
```
Lift = CL × ½ × ρ × V² × S

Where:
CL = Coefficient of lift
ρ = Air density
V = Velocity
S = Wing area
```

**Factors Affecting Lift**:
1. **Airspeed**: Lift increases with square of velocity
2. **Air Density**: Higher density = more lift
3. **Wing Area**: Larger wings = more lift
4. **Angle of Attack**: Increases lift until stall
5. **Wing Shape**: Airfoil design affects efficiency

### Drag

**Types of Drag**:

**Parasite Drag**: Resistance from non-lifting surfaces
- **Form Drag**: Shape resistance
- **Skin Friction**: Surface roughness
- **Interference Drag**: Airflow disruption at junctions
- Increases with square of velocity

**Induced Drag**: Byproduct of lift generation
- Created by wingtip vortices
- Decreases as airspeed increases
- Higher at high angles of attack (slow flight)

**Total Drag**: Sum of parasite and induced drag
- Minimum drag at specific airspeed (L/D max)
- Best glide speed occurs at minimum drag

### Stalls

**Definition**: Occurs when wing exceeds critical angle of attack

**Characteristics**:
- Airflow separates from upper wing surface
- Sudden loss of lift
- Increase in drag
- Can occur at any airspeed or attitude
- Can occur at any power setting

**Stall Speed Factors**:
- **Weight**: Heavier aircraft stalls at higher speed
- **Load Factor**: Turns increase stall speed (Vs × √n)
- **Power**: Power-on stalls occur at lower speed
- **CG Position**: Aft CG increases stall speed
- **Flaps**: Flaps decrease stall speed

**Stall Recovery**:
1. Reduce angle of attack (push forward on yoke)
2. Add full power
3. Level wings with coordinated rudder
4. Return to level flight

**Spin**: Aggravated stall with rotation
- Requires stall + yaw
- "If you don't stall, you can't spin"
- Recovery: PARE (Power idle, Ailerons neutral, Rudder opposite, Elevator forward)

### Stability

**Three Axes of Rotation**:
- **Longitudinal (Roll)**: Controlled by ailerons
- **Lateral (Pitch)**: Controlled by elevator
- **Vertical (Yaw)**: Controlled by rudder

**Types of Stability**:
- **Positive**: Returns to original state after disturbance
- **Neutral**: Remains in new state
- **Negative**: Continues to diverge (unstable)

**Design Features for Stability**:
- **Longitudinal**: Horizontal stabilizer, CG forward of center of lift
- **Lateral**: Dihedral (upward wing angle), keel effect
- **Directional**: Vertical stabilizer (fin)

### Load Factor

**Definition**: Ratio of lift to weight (G-force)

**Level Flight**: Load factor = 1G
**60° Bank**: Load factor = 2G (stall speed increases by 41%)
**Maneuvering Speed (Va)**: Maximum speed for full control deflection

**V-G Diagram**: Shows aircraft structural limits
- **Green Arc**: Normal operating range
- **Yellow Arc**: Caution range (smooth air only)
- **Red Line**: Never exceed speed (Vne)

## Aircraft Systems

### Powerplant

**Four-Stroke Engine Cycle**:
1. **Intake**: Piston down, intake valve open, fuel-air mixture enters
2. **Compression**: Both valves closed, piston up, mixture compressed
3. **Power**: Spark ignites mixture, piston forced down
4. **Exhaust**: Exhaust valve opens, piston up, gases expelled

**Engine Components**:
- **Cylinders**: Contain combustion
- **Pistons**: Convert pressure to motion
- **Crankshaft**: Converts linear to rotational motion
- **Camshaft**: Opens/closes valves
- **Magnetos**: Provide ignition spark (dual system for redundancy)
- **Spark Plugs**: Ignite fuel-air mixture (two per cylinder)

**Engine Instruments**:
- **Tachometer**: Engine RPM
- **Oil Pressure**: Lubrication system health
- **Oil Temperature**: Engine cooling
- **Cylinder Head Temperature (CHT)**: Hottest cylinder
- **Exhaust Gas Temperature (EGT)**: Mixture monitoring

### Fuel System

**Components**:
- **Fuel Tanks**: Store fuel (typically in wings)
- **Fuel Selector**: Choose tank or OFF
- **Fuel Pump**: Engine-driven (mechanical) and electric (backup)
- **Fuel Strainer**: Removes water and contaminants
- **Fuel Lines**: Transport fuel to engine

**Fuel Grades**:
- **100LL (Low Lead)**: Blue color, most common for piston aircraft
- **Jet A**: Kerosene-based, for turbine engines (NOT for piston engines)

**Fuel Management**:
- Check fuel quantity before flight
- Monitor fuel consumption
- Switch tanks as required
- Use fuel selector properly
- Drain sumps to check for water/contamination

### Carburetor and Carburetor Ice

**Carburetor Function**: Mixes fuel and air in proper ratio

**Carburetor Ice**:
- Forms when moisture freezes in venturi
- Temperature drop due to fuel vaporization and pressure decrease
- Can occur at temperatures up to 70°F with visible moisture
- **Symptoms**: Loss of RPM, rough running
- **Prevention/Cure**: Carburetor heat (uses hot air from exhaust)

**Carburetor Heat**:
- Pulls hot, unfiltered air from around exhaust
- Expect RPM drop when applied (less dense air)
- Use as needed or as recommended by POH
- Full hot or full cold (not partial)

### Electrical System

**Components**:
- **Battery**: Provides power for starting and backup
- **Alternator/Generator**: Produces electrical power during operation
- **Voltage Regulator**: Maintains proper voltage
- **Ammeter/Loadmeter**: Shows electrical system status
- **Circuit Breakers/Fuses**: Protect circuits from overload
- **Master Switch**: Controls electrical system

**Electrical Failure**:
- Battery provides limited backup power
- Conserve electrical power (turn off non-essential equipment)
- Land as soon as practical

### Pitot-Static System

**Pitot Tube**: Measures ram air pressure (dynamic pressure)
**Static Port**: Measures ambient air pressure (static pressure)

**Instruments Using Pitot-Static**:

**Airspeed Indicator**:
- Uses both pitot and static pressure
- Shows indicated airspeed (IAS)
- **Pitot Blockage**: Airspeed reads zero or freezes
- **Static Blockage**: Erroneous readings, acts like altimeter

**Altimeter**:
- Uses static pressure only
- Shows height above sea level (when set to local altimeter setting)
- **Kollsman Window**: Adjustable for barometric pressure
- **Static Blockage**: Altimeter freezes

**Vertical Speed Indicator (VSI)**:
- Uses static pressure only
- Shows rate of climb or descent (feet per minute)
- **Lag**: 6-9 second delay
- **Static Blockage**: Reads zero

**Pitot Heat**: Prevents ice formation in pitot tube

### Vacuum System

**Purpose**: Powers gyroscopic instruments

**Components**:
- **Vacuum Pump**: Engine-driven, creates suction
- **Vacuum Gauge**: Shows system pressure (typically 4.5-5.5 inches Hg)
- **Air Filter**: Protects instruments

**Vacuum-Powered Instruments**:
- **Attitude Indicator**: Shows pitch and bank
- **Heading Indicator**: Shows magnetic heading
- **Turn Coordinator** (sometimes electric)

**Vacuum Failure**:
- Gyro instruments become unreliable
- Use magnetic compass and turn coordinator
- Declare emergency if IMC

### Propeller

**Function**: Converts engine power to thrust

**Fixed-Pitch Propeller**:
- Blade angle cannot be changed
- Simple, reliable
- Optimized for one flight regime

**Constant-Speed Propeller**:
- Blade angle adjustable in flight
- Maintains constant RPM
- More efficient across flight regimes
- Controlled by propeller control (blue knob)

**P-Factor (Asymmetric Thrust)**:
- At high angles of attack, descending blade has higher AOA
- Creates yawing moment to left (in U.S. aircraft)
- Most pronounced at low airspeed, high power

**Torque Effect**:
- Newton's Third Law: engine turns prop clockwise, aircraft wants to roll left
- Countered by aileron or asymmetric design

**Slipstream Effect**:
- Spiraling propwash strikes left side of vertical stabilizer
- Creates left-turning tendency
- Countered by rudder

**Gyroscopic Precession**:
- Force applied to spinning propeller manifests 90° ahead in direction of rotation
- Affects tailwheel aircraft during takeoff (tail rises, prop disc tilts, yaw left)

## Aircraft Performance

### Density Altitude

**Definition**: Pressure altitude corrected for non-standard temperature

**High Density Altitude** (hot, high, humid):
- Reduced engine power
- Reduced propeller efficiency
- Reduced lift
- Longer takeoff distance
- Reduced climb rate
- Longer landing distance

**Factors Increasing Density Altitude**:
- High elevation
- High temperature
- High humidity
- Low barometric pressure

**Performance Impact**:
- Every 1,000 ft increase in density altitude = ~10% performance loss

### Weight and Balance

**Center of Gravity (CG)**: Point where aircraft balances

**CG Limits**:
- **Forward CG**: 
  - More stable
  - Higher stall speed
  - Reduced elevator effectiveness
  - Longer takeoff distance
- **Aft CG**:
  - Less stable
  - Lower stall speed
  - Risk of unrecoverable spin
  - Reduced longitudinal stability

**Weight Limits**:
- **Maximum Gross Weight**: Maximum authorized weight
- **Empty Weight**: Weight of aircraft with unusable fuel/oil
- **Useful Load**: Maximum gross weight - empty weight
- **Payload**: Useful load - usable fuel

**Weight and Balance Calculation**:
```
Moment = Weight × Arm
CG = Total Moment / Total Weight

Must be within CG envelope for safe flight
```

### Takeoff and Landing Performance

**Factors Affecting Takeoff Distance**:
- Weight (heavier = longer)
- Density altitude (higher = longer)
- Wind (headwind = shorter, tailwind = longer)
- Runway surface (grass/soft = longer)
- Runway slope (uphill = longer)
- Flaps (as recommended by POH)

**Factors Affecting Landing Distance**:
- Weight (heavier = longer)
- Density altitude (higher = longer)
- Wind (headwind = shorter, tailwind = longer)
- Runway surface (grass/soft/wet = longer)
- Runway slope (downhill = longer)
- Approach speed (faster = longer)

**Performance Charts**: Use POH for specific aircraft

## Best Practices

1. **Understand Your Aircraft**: Study POH thoroughly
2. **Preflight Inspection**: Check all systems before flight
3. **Monitor Instruments**: Scan regularly during flight
4. **Respect Limitations**: Stay within aircraft limits
5. **Plan for Performance**: Calculate takeoff/landing distances
6. **Maintain Proficiency**: Practice stalls, slow flight, emergency procedures

## Conclusion

Mastery of aerodynamics and aircraft systems is essential for safe flight operations. Understanding how aircraft fly, how systems work, and how performance varies with conditions enables pilots to make informed decisions and operate aircraft safely and efficiently.
