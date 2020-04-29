from naoqi import ALProxy
import confNAO

def do(direcao):

	names = list()
	times = list()
	keys = list()

	if direcao is 1: # Esquerda 1
		names.append("HeadPitch")
		times.append([ 0.349])
		keys.append([ [ 0.33437, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("HeadYaw")
		times.append([ 0.20000])
		keys.append([ [ 1.24557, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

	elif direcao is 2: # Esquerda 2
		names.append("HeadPitch")
		times.append([ 0.349])
		keys.append([ [ 0.33859, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("HeadYaw")
		times.append([ 0.20000])
		keys.append([ [ 0.77309, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

	elif direcao is 3: # Esquerda 3
		names.append("HeadPitch")
		times.append([ 0.349])
		keys.append([ [ 0.26529, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("HeadYaw")
		times.append([ 0.20000])
		keys.append([ [ 0.33284, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

	elif direcao is 4: # Direita 3
		names.append("HeadPitch")
		times.append([ 0.349])
		keys.append([ [ 0.30718, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("HeadYaw")
		times.append([ 0.20000])
		keys.append([ [ -0.30991, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

	elif direcao is 5: # Direita 2
		names.append("HeadPitch")
		times.append([ 0.349])
		keys.append([ [ 0.41874, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("HeadYaw")
		times.append([ 0.20000])
		keys.append([ [ -0.79312, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

	elif direcao is 6: # Direita 1
		names.append("HeadPitch")
		times.append([ 0.349])
		keys.append([ [ 0.38192, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("HeadYaw")
		times.append([ 0.20000])
		keys.append([ [ -1.09839, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

	elif direcao is 7: # Direita 2
		names.append("HeadPitch")
		times.append([ 0.349])
		keys.append([ [ 0.41874, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("HeadYaw")
		times.append([ 0.20000])
		keys.append([ [ -0.79312, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

	elif direcao is 8: # Direita 3
		names.append("HeadPitch")
		times.append([ 0.349])
		keys.append([ [ 0.30718, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

		names.append("HeadYaw")
		times.append([ 0.20000])
		keys.append([ [ -0.30991, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

	elif direcao is 9: # Esquerda 3
                names.append("HeadPitch")
                times.append([ 0.349])
                keys.append([ [ 0.26529, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

                names.append("HeadYaw")
                times.append([ 0.20000])
                keys.append([ [ 0.33284, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])


	elif direcao is 10: # Esquerda 2
                names.append("HeadPitch")
                times.append([ 0.349])
                keys.append([ [ 0.33859, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

                names.append("HeadYaw")
                times.append([ 0.20000])
                keys.append([ [ 0.77309, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])
	try:
		motion = ALProxy("ALMotion", confNAO.ip_addr,confNAO.port_num)
		motion.angleInterpolationBezier(names, times, keys);
		return(True)

	except BaseException, err:
		print err
		return(False)
