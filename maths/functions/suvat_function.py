from .quadratic_function import quadratic
def suvat(s,u,v,a,t,solve_for,remove):
    try:
        
        temp = [s,u,v,a,t]
        print(temp)
        for i in range(len(temp)):
            if temp[i] != None:
                temp[i] = float(temp[i])
            elif temp[i] == None:
                temp[i] == "n"
        
        print(temp)
        s,u,v,a,t = temp
        print(s,u,v,a,t)
        print(remove)
        print("Start")
        if remove == "s":
            #v=u+at
            if solve_for == "v":
                v = u + a*t
                return v
            elif solve_for == "u":
                u = v - a*t
                return u
            elif solve_for == "a":
                a = (v-u)/t
                return a
            elif solve_for == "t":
                t = (v-u)/a
                return t
        elif remove == "u":
            #s=v*t-0.5*a*(t**2)
            if solve_for == "s":
                s = v*t - 0.5*a*(t**2)
                return s
            elif solve_for == "v":
                v = (s + 0.5*a*(t**2))/t
                return v
            elif solve_for == "a":
                a = ((v*t)-s)/(0.5*(t**2))
                return a
            elif solve_for == "t":
                #quadratic -0.5*a*t^2 -v*t -s = 0
                t1,t2,err_msg = quadratic((-0.5*a),v,-s)
                if err_msg == "no real roots":
                    # raise something
                    return "no real roots"
                elif t1 < 0 and t2 < 0:
                    return "time is less than 0"
                return f"{t1},{t2}"
        elif remove == "v":
            # s = u*t + 0.5*a*(t**2)
            if solve_for == "s":
                s = u*t + 0.5*a*(t**2)
            elif solve_for == "u":
                u = (s - (0.5*a*(t**2)))/t
            elif solve_for == "a":
                a = ((s-(u*t))/(0.5*(t**2)))
                print("here")
                print(a)
            elif solve_for == "t":
                #quadratic 0.5*a*t^2 + u*t -s = 0
                t1,t2,err_msg = quadratic((0.5*a),u,-s)
                if err_msg == "no real roots":
                    # raise something
                    return "no real roots"
                elif t1 < 0 and t2 < 0:
                    return "time is less than 0"
                return f"t={t1},t={t2}"
        elif remove == "a":
            # s = 0.5*(u+v)*t
            if solve_for == "s":
                s = 0.5*(u+v)*t
                return s
            elif solve_for == "u":
                u = ((s*2)/t)-v
                return u
            elif solve_for == "v":
                v = ((s*2)/t)-u
                return v
            elif solve_for == "t":
                t = s/(0.5*(u+v))
                if t < 0:
                    return "time is less than 0"
                return t
        elif remove == "t":
            # v**2 = u**2 + 2*a*s
            if solve_for == "s":
                s = ((v**2)-(u**2))/(2*a)
                return s
            elif solve_for == "u":
                u = ((v**2)-(2*a*s))**0.5
                return u
            elif solve_for == "v":
                v = (u**2 + 2*a*s)**0.5
                return v
            elif solve_for == "a":
                a = ((v**2)-(u**2))/(2*s)
                return a
    except ZeroDivisionError:
        return "invalid input, cant divide by 0"
    except TypeError:
        return "Numbers only"
    else:
      return "invalid input else"