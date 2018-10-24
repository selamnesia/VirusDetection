#coding:utf-8
import pefile
import argparse
import sys
 
DEBUG = 0;
isDirty = 0;
 
# 从PE文件中提取数据值并将其作为成员变量保存的类
class PEFile:
	def __init__(self,filename):
		self.pe =  pefile.PE(filename,fast_load=True)
		self.filename=filename
		self.DebugSize 		= self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].Size
		self.ImageVersion	= ((self.pe.OPTIONAL_HEADER.MajorImageVersion*100)+self.pe.OPTIONAL_HEADER.MinorImageVersion)*1000#操作系统版本号
		self.IatRVA			= self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[1].VirtualAddress#Import Address Table中根据IMAGE_SECTION_HEADER 中的VirtualAddress 字段
		self.ExportSize		= self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].Size
		self.ResourceSize	= self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[2].Size#源大小
		self.VirtualSize2	= self.pe.sections[1].Misc_VirtualSize
		self.NumberOfSections = self.pe.FILE_HEADER.NumberOfSections		
	def DataDump(self):
		print('Starting dump of ' + self.filename)
		print('DebugSize:\t\t' + str(self.DebugSize )) 
		print('ImageVersion:\t\t' + str(self.ImageVersion)) 
		print('IatRVA:\t\t' + str(self.IatRVA)) 
		print('ExportSize:\t\t' + str(self.ExportSize)) 
		print('ResourceSize:\t\t' + str(self.ResourceSize)) 
		print('VirtualSize2:\t\t' + str(self.VirtualSize2)) 
		print('NumberOfSections:\t' + str(self.NumberOfSections)) 
		print('Stop')
 
def printResult(classification):
	if classification == 0:
		print ('恶意代码:\t0')
	else:
		print ('恶意代码:\t1')

#J48()：C4.5决策树算法（决策树在分析各个属性时，是完全独立的）		weka
def runJ48():
	isDirty = 0
	if input.DebugSize <=0:
		if input.ExportSize <= 211:
			if input.ImageVersion <= 520:
				if input.VirtualSize2 <= 130:
					if input.VirtualSize2 <= 5:
						if input.ResourceSize <= 37520:
							isDirty = 1
						elif input.ResourceSize > 37520:
							if input.NumberOfSections <= 2:
								if input.IatRVA <= 2048:
									isDirty = 0
								else:
									isDirty = 1
							else:
								isDirty = 1
					else:
						if input.VirtualSize2 <= 12:
							if input.NumberOfSections <= 3:
								isDirty = 0
							else:
								isDirty = 1
						else:
							isDirty = 1
				else:
					isDirty = 1
			else:
				if input.ResourceSize <= 0:
					if input.ImageVersion <= 1000:
						if input.NumberOfSections <= 4:
							isDirty = 1
						else:
							if input.ExportSize <= 74:
								if input.VirtualSize2 <= 1556:
									isDirty = 1
								else:
									isDirty = 0
							else:
								isDirty = 0
					else:
						isDirty = 1
				else:
					if input.NumberOfSections <= 2:
						if input.ImageVersion <= 3420:
							isDirty = 1
						else:
							isDirty = 0
					else:
						isDirty = 1
		else:
			if input.ImageVersion <= 0:
				if input.ExportSize <= 23330:
					if input.IatRVA <= 98304:
						if input.NumberOfSections <= 3:
							isDirty = 1
						else:
							if input.IatRVA <= 53872:
								isDirty = 0
							else:
								if input.ExportSize <= 273:
									isDirty = 1
								else:
									if input.ResourceSize <= 1016:
										isDirty = 1
									else:
										isDirty = 0
					else:
						isDirty = 0
				else:
					isDirty = 1
			else:
				isDirty = 0
	else:
		if input.ResourceSize <= 545:
			if input.ExportSize <= 92:
				if input.NumberOfSections <= 4:	
					isDirty = 0
				else:
					isDirty = 1
		else:
			if input.IatRVA <= 94208:
				if input.NumberOfSections <= 5:
					if input.ExportSize <= 0:
						if input.NumberOfSections <= 4:
							if input.IatRVA <= 13504:
								if input.ImageVersion <= 353:
									if input.NumberOfSections <= 3:
										if input.IatRVA <= 6144:
											if input.IatRVA <= 2048:
												isDirty = 0
											else:
												if input.VirtualSize2 <= 496:
													isDirty = 1
												else:
													isDirty = 0
										else:
											isDirty = 0
									else:
										if input.DebugSize <= 41:
											if input.ResourceSize <= 22720:
												isDirty = 1
											else:
												isDirty = 0
										else:
											isDirty = 0
								else:
									isDirty = 0
							else:
								if input.ResourceSize <= 35328:
									isDirty = 0
								else:
									isDirty = 1
						else:
							if input.IatRVA <= 2048:
								isDirty = 1
							else:
								isDirty = 0
					else:
						isDirty = 0
				else:
					if input.IatRVA <= 1054:
						if input.ExportSize <= 218:
							if input.IatRVA <= 704:
								isDirty = 1
							else:
								if input.NumberOfSections <= 6:
									isDirty = 1
								else:
									isDirty = 0
						else:
							isDirty = 0
					else:
						isDirty = 0
			else:
				if input.ExportSize <= 0:
					if input.VirtualSize2 <= 78800:
						if input.NumberOfSections <= 4:
							isDirty = 0
						else:
							if input.ImageVersion <= 2340:
								if input.ResourceSize <= 7328:
									isDirty = 1
								else:
									isDirty = 0
							else:
								isDirty = 0
					else:
						isDirty = 1
				else:
					if input.IatRVA <= 106496:
						if input.ResourceSize <= 2800:
							isDirty = 0
						else:
							isDirty = 1
					else:
						isDirty = 0
	return isDirty
# 如果是未分类的结果，可能需要添加isDirty = 0语句					
 
def runJ48Graft():
	isDirty = 0
	if input.DebugSize <=0:
		if input.ExportSize <= 211:
			if input.ImageVersion <= 520:
				if input.VirtualSize2 <= 130:
					if input.VirtualSize2 <= 5:
						if input.ResourceSize <= 37520:
							isDirty = 1
						elif input.ResourceSize > 37520:
							if input.NumberOfSections <= 2:
								if input.IatRVA <= 2048:
									if input.ExportSize <= 67.5:
										isDirty = 0
									else:								
										isDirty = 1
								else:
									isDirty = 1
							else:
								isDirty = 1
					else:
						if input.VirtualSize <= 12:
							if input.NumberOfSections <= 3:
								isDirty = 0
							else:
								isDirty = 1
						else:
							isDirty = 1
				else:
					isDirty = 1
			else:
				if input.ResourceSize <= 0:
					if input.ImageVersion <= 1000:
						if input.NumberOfSections <= 4:
							isDirty = 1
						else:
							if input.ExportSize <= 74:
								if input.VirtualSize2 <= 1556:
									isDirty = 1
								else:
									if input.IatRVA <= 5440:
										if input.VirtualSize2 <= 126474:
											if input.ExportSize <= 24:
												isDirty = 0
											else:
												isDirty = 1
										else:
											isDirty = 1
									else:
										isDirty = 1
							else:
								isDirty = 0
					else:
						isDirty = 1
				else:
					if input.NumberOfSections <= 2:
						if input.ImageVersion <= 3420:
							isDirty = 1
						else:
							isDirty = 0
					else:
						isDirty = 1
		else:
			if input.ImageVersion <= 0:
				if input.ExportSize <= 23330:
					if input.IatRVA <= 98304:
						if input.NumberOfSections <= 3:
							isDirty = 1
						else:
							if input.IatRVA <= 53872:
								if input.VirtualSize2 <= 17.5:
									isDirty = 1
								else:
									if input.NumberOfSections <= 10.5:
										if input.ResourceSize <= 3103192:
											if input.ExportSize <= 10858.5:
												if input.VirtualSize2 <= 116016.5:
													isDirty = 0
												else:
													isDirty = 1
											else:
												isDirty = 0
										else:
											isDirty = 1
									else:
										isDirty = 1
							else:
								if input.ExportSize <= 273:
									isDirty = 1
								else:
									if input.ResourceSize <= 1016:
										isDirty = 1
									else:
										isDirty = 0
					else:
						isDirty = 0
				else:
					isDirty = 1
			else:
				if input.ExportSize <= 1006718985:
					isDirty = 0
				else:
					isDirty = 1
	else:
		if input.ResourceSize <= 545:
			if input.ExportSize <= 92:
				if input.NumberOfSections <= 4:	
					isDirty = 0
				else:
					if input.ImageVersion <= 6005:
						if input.ExportSize <= 6714:
							isDirty = 1
						else:
							isDirty = 0
					else:
						isDirty = 0							
		else:
			if input.IatRVA <= 94208:
				if input.NumberOfSections <= 5:
					if input.ExportSize <= 0:
						if input.NumberOfSections <= 4:
							if input.IatRVA <= 13504:
								if input.ImageVersion <= 353:
									if input.NumberOfSections <= 3:
										if input.IatRVA <= 6144:
											if input.IatRVA <= 2048:
												if input.ResourceSize <= 934:
													isDirty = 1
												else:
													if input.VirtualSize2 <= 2728:
														isDirty = 0
													else:
														isDirty = 1
											else:
												if input.VirtualSize2 <= 496:
													isDirty = 1
												else:
													isDirty = 0
										else:
											isDirty = 0
									else:
										if input.DebugSize <= 41: # debug here
											if input.ResourceSize <= 22720:
												if input.IatRVA <= 2048:
													isDirty = 1
												else:
													if input.VirtualSize2 <= 46:
														isDirty = 0
													else:
														isDirty = 1
											else:
													if input.VirtualSize2 <= 43030:
														if input.ResourceSize <= 3898348:
															if input.IatRVA <= 2048:
																isDirty = 1
															else:
																isDirty = 0
														else:
															isDirty = 1
													else:
														isDirty = 0
										else:
											isDirty = 0
								else:
									isDirty = 0
							else:
								if input.ResourceSize <= 35328:
									if input.ImageVersion <= 4005:
										if input.NumberOfSections <= 1.5:
											isDirty = 1
										else:
											isDirty = 0
									else:
										isDirty = 0
								else:
									if input.ImageVersion <= 5510:
										if input.DebugSize <= 42:
											if input.VirtualSize2 <= 144328:
												if input.NumberOfSections <= 3.5:
													isDirty = 0
												else:
													isDirty = 1
											else:
												isDirty = 0
										else:
											isDirty = 0
									else:
										isDirty = 0										
						else:
							if input.IatRVA <= 2048:
								isDirty = 1
							else:
								isDirty = 0
					else:
						isDirty = 0
				else:
					if input.IatRVA <= 1054:
						if input.ExportSize <= 218:
							if input.IatRVA <= 704:
								isDirty = 1
							else:
								if input.NumberOfSections <= 6:
									isDirty = 1
								else:
									isDirty = 0
						else:
							if input.ExportSize <= 1006699445:
								if input.ImageVersion <= 5510:
									if input.ImageVersion <= 500:
										isDirty = 1
									else:
										isDirty = 0
								else:
									isDirty = 0
							else:
								isDirty = 1
					else:
						isDirty = 0
			else:
				if input.ExportSize <= 0:
					if input.VirtualSize2 <= 78800:
						if input.NumberOfSections <= 4:
							isDirty = 0
						else:
							if input.ImageVersion <= 2340:
								if input.ResourceSize <= 7328:
									isDirty = 1
								else:
									if input.VirtualSize2 <= 8288.5:
										isDirty = 1
									else:
										if input.NumberOfSections <= 6.5:
											isDirty = 0
										else:
											isDirty = 1
							else:
								isDirty = 0
					else:
						if input.ImageVersion <= 5515:
							isDirty = 1
						else:
							isDirty = 0
				else:
					if input.IatRVA <= 106496:
						if input.ResourceSize <= 2800:
							isDirty = 0
						else:
							if input.ImageVersion <= 500:
								if input.ResourceSize <= 5360:
									if input.NumberOfSections <= 4.5:
										isDirty = 0
									else:
										if input.VirtualSize2 <= 22564.5:
											if input.ExportSize <= 191.5:
												if input.DebugSize <= 42:
													if input.ExportSize <= 162.5:
														isDirty = 0
													else:
														if input.VirtualSize2 <= 10682:
															isDirty = 0
														else:
															if input.ResourceSize <= 3412:
																isDirty = 0
															else:
																isDirty = 1
												else:
													isDirty = 0
											else:
												isDirty = 0
										else:
											isDirty = 0
								else:
									isDirty = 0
							else:
								isDirty = 0
					else:
						isDirty = 0
	return isDirty
# 如果是未分类的结果，可能需要添加isDirty = 0语句					
 
def runPART():
	isDirty = 0
	if input.DebugSize > 0  and input.ResourceSize > 545 and input.IatRVA <= 94208 and input.NumberOfSections <= 5 and input.ExportSize > 0 and input.NumberOfSections > 3:
		isDirty = 0
	elif input.DebugSize <=0 and input.ImageVersion <= 4900 and input.ExportSize <= 71 and input.ImageVersion <= 520 and input.VirtualSize2 > 130 and input.IatRVA <= 24576:
		isDirty = 1
	elif input.DebugSize <=0 and input.ImageVersion <= 4900 and input.ExportSize <= 211 and input.ResourceSize <= 32272 and input.NumberOfSections <= 10 and input.VirtualSize2 <= 5 and input.ImageVersion <= 3420:
		isDirty = 1
	elif input.DebugSize > 0 and input.ResourceSize > 598 and input.VirtualSize2 <= 105028 and input.VirtualSize2 > 1 and input.ImageVersion > 5000:
		isDirty = 0
	elif input.IatRVA <= 0 and input.ImageVersion > 4180 and input.ResourceSize > 2484:
		isDirty = 0
	elif input.DebugSize <= 0 and input.NumberOfSections <= 1 and input.ResourceSize > 501:
		isDirty = 0
	elif input.DebugSize <= 0 and input.ExportSize <= 211 and input.NumberOfSections > 2 and input.ImageVersion > 1000 and input.ResourceSize <= 12996:
		isDirty = 1
	elif input.DebugSize <= 0 and input.ExportSize <= 211 and input.NumberOfSections > 2 and input.ResourceSize > 0 and input.VirtualSize2 > 1016:
		isDirty = 1
	elif input.NumberOfSections > 8 and input.VirtualSize2 <= 2221: 
		isDirty = 1
	elif input.ResourceSize <= 736 and input.NumberOfSections <= 3: 
		isDirty = 1
	elif input.NumberOfSections <= 3 and input.IatRVA > 4156: 
		isDirty = 0
	elif input.ImageVersion <= 6000 and input.ResourceSize <= 523 and input.IatRVA > 0 and input.ExportSize <= 95: 
		isDirty = 1
	elif input.ExportSize <= 256176 and input.DebugSize > 0 and input.ImageVersion <= 5450 and input.IatRVA > 1664 and input.ResourceSize <= 2040 and input.DebugSize <= 41: 
		isDirty = 0
	elif input.ExportSize <= 256176 and input.ImageVersion > 5450: 
		isDirty = 0
	elif input.ExportSize > 256176:
		isDirty = 1
	elif input.ImageVersion > 0 and input.ResourceSize > 298216 and input.IatRVA <= 2048:
		isDirty = 1
	elif input.ImageVersion > 0 and input.ExportSize > 74 and input.DebugSize > 0:
		isDirty = 0
	elif input.ImageVersion > 0 and input.VirtualSize2 > 4185 and input.ResourceSize <= 215376 and input.IatRVA <= 2048 and input.NumberOfSections <= 5:
		isDirty = 0
	elif input.ImageVersion > 1010 and input.DebugSize <= 56 and input.VirtualSize2 <= 215376:
		isDirty = 0
	elif input.ExportSize > 258 and input.NumberOfSection > 3 and input.DebugSize > 0:
		isDirty = 0
	elif input.ExportSize > 262 and input.ImageVersion > 0 and input.NumberOfSections > 7:
		isDirty = 0
	elif input.DebugSize > 41 and input.NumberOfSections <= 4:
		isDirty = 0
	elif input.ExportSize <= 262 and input.NumberOfSections > 3 and input.VirtualSize2 <= 37:
		isDirty = 1
	elif input.VirtualSize2 > 40 and input.ExportSize <= 262 and input.DebugSize <= 0 and input.ImageVersion <= 353 and input.ExportSize <= 142:
		isDirty = 1
	elif input.VirtualSize2 > 72384 and input.VirtualSize2 <= 263848:
		isDirty = 1
	elif input.IatRVA > 106496 and input.IatRVA <= 937984 and input.DebugSize > 0 and input.ResourceSize > 4358:
		isDirty = 0
	elif input.VirtualSize2 <= 64 and input.IatRVA <= 2048 and input.DebugSize <= 0 and input.ImageVersion <= 353 and input.ExportSize <= 0 and input.VirtualSize2 <= 4 and input.NumberOfSections <= 2:
		isDirty = 0
	elif input.DebugSize <= 0 and input.NumberOfSections <= 4 and input.IatRVA > 45548:
		isDirty = 1
	elif input.DebugSize > 0 and input.DebugSize <= 56 and input.IatRVA <= 94208 and input.ResourceSize <= 4096:
		isDirty = 1
	elif input.DebugSize <= 0 and input.IatRVA <= 98304 and input.NumberOfSections > 6 and input.ResourceSize <= 864 and input.ExportSize > 74 and input.ImageVersion > 353 and input.ExportSize <= 279:
		isDirty = 0
	elif input.DebugSize <= 0 and input.IatRVA <= 98304 and input.NumberOfSections <= 2 and input.ResourceSize <= 1264128:
		isDirty = 1
	elif input.VirtualSize2 <= 64 and input.IatRVA <= 2048 and input.DebugSize > 0:
		isDirty = 0
	elif input.ExportSize <= 276 and input.NumberOfSections > 5 and input.ResourceSize <= 1076:
		isDirty = 0
	elif input.DebugSize > 0 and input.IatRVA <= 94208 and input.ExportSize <= 82 and input.DebugSize <= 56 and input.NumberOfSections > 2 and input.ImageVersion <= 2340 and input.ResourceSize <= 118280 and input.VirtualSize2 > 5340:
		isDirty = 0
	elif input.DebugSize > 0 and input.ImageVersion <= 2340 and input.DebugSize <= 56 and input.NumberOfSections > 3 and input.VirtualSize2 > 360 and input.NumberOfSections <= 5:
		isDirty = 1
	elif input.IatRVA > 37380 and input.ImageVersion <= 0 and input.NumberOfSections <= 5 and input.VirtualSize2 > 15864:
		isDirty = 0
	elif input.DebugSize <= 0 and input.VirtualSize2 <= 80 and input.IatRVA <= 4096 and input.ExportSize <= 0 and input.VirtualSize2 > 4 and input.VirtualSize2 <= 21:
		isDirty = 0
	elif input.DebugSize <= 0:
		isDirty = 1
	elif input.ExportSize <= 82 and input.DebugSize <= 56 and input.NumberOfSections <= 5 and input.NumberOfSections > 2 and input.IatRVA <= 6144 and input.ImageVersion > 2340:
		isDirty = 0
	elif input.ImageVersion > 2340:
		isDirty = 1
	elif input.ResourceSize > 5528:
		isDirty = 0
	else:
		isDirty = 1
	return isDirty
 
	
def runRidor():
	isDirty = 0
	#Except (DebugSize <= 14) and (ImageVersion <= 760) and (VirtualSize2 > 992) and (ExportSize <= 80.5) => isDirty = 1  (1702.0/16.0) [855.0/5.0]
	if input.DebugSize <= 14 and input.ImageVersion <= 760 and input.VirtualSize2 > 992 and input.ExportSize <= 80.5:
		isDirty = 1
#Except (DebugSize <= 14) and (ImageVersion <= 4525) and (ExportSize <= 198.5) and (ResourceSize <= 37532) and (VirtualSize2 <= 6) and (ResourceSize <= 7348) and (ResourceSize > 1773) => isDirty = 1  (106.0/0.0) [48.0/0.0]
	elif input.DebugSize <= 14 and input.ImageVersion <= 4525  and input.ExportSize <= 198.5 and input.ResourceSize <= 7348 and input.VirtualSize2 <=6 and input.ResourceSize > 1773:
		isDirty = 1
#Except (DebugSize <= 14) and (ImageVersion <= 4950) and (ExportSize <= 192) and (IatRVA > 256) and (VirtualSize2 > 42) and (ExportSize <= 56) and (NumberOfSections > 3.5) => isDirty = 1  (193.0/0.0) [91.0/0.0]
	elif input.DebugSize <= 14 and input.ImageVersion <= 4950 and input.ExportSize <= 56 and input.IatRVA > 256 and input.VirtualSize2 > 42 and input.NumberOfSections > 3.5:
		isDirty = 1
#Except (DebugSize <= 14) and (ImageVersion <= 4950) and (VirtualSize2 <= 6) and (ResourceSize <= 37532) and (ResourceSize <= 17302) => isDirty = 1  (388.0/0.0) [216.0/7.0]
	elif input.DebugSize <= 14 and input.ImageVersion <= 4950 and input.VirtualSize2 <= 6 and input.ResourceSize > 17302:
		isDirty = 1
#Except (DebugSize <= 14) and (NumberOfSections > 2.5) and (ResourceSize > 1776) and (IatRVA <= 6144) and (ExportSize <= 219.5) and (VirtualSize2 > 2410) and (VirtualSize2 <= 61224) => isDirty = 1  (238.0/0.0) [116.0/0.0]
	elif input.DebugSize <= 14 and input.NumberOfSections >= 2.5 and input.ResourceSize <= 1776 and input.IatRVA <= 6144 and input.ExportSize <= 219.5 and input.VirtualSize2 > 2410 and input.VirtualSize2 <= 61224:
		isDirty = 1
#Except (DebugSize <= 14) and (NumberOfSections > 2.5) and (ExportSize <= 198) and (ResourceSize > 8) and (VirtualSize2 > 83) and (ResourceSize <= 976) => isDirty = 1  (151.0/2.0) [83.0/2.0]
	elif input.DebugSize <= 14 and input.NumberOfSections >= 2.5 and input.ExportSize  <= 198 and input.ResourceSize > 8 and input.VirtualSize2 > 83 and input.ResourceSize <= 976:
		isDirty = 1
#Except (DebugSize <= 14) and (NumberOfSections > 2.5) and (ResourceSize > 1418) and (IatRVA <= 6144) and (VirtualSize2 <= 4) => isDirty = 1  (94.0/0.0) [44.0/0.0]
	elif input.DebugSize <= 14 and input.NumberOfSections >= 2.5 and input.ResourceSize > 1418 and input.IatRVA > 6144 and input.VirtualSize2 <= 4:
		isDirty = 1
#Except (DebugSize <= 14) and (VirtualSize2 > 14) and (NumberOfSections <= 4.5) and (ResourceSize > 8) and (VirtualSize2 <= 2398) and (ResourceSize > 1550) => isDirty = 1  (84.0/0.0) [41.0/1.0]
	elif input.DebugSize <= 14 and input.VirtualSize2 > 14 and input.NumberOfSections > 4.5 and input.ResourceSize > 1550 and input.VirtualSize2 <= 2398:
		isDirty = 1
#Except (DebugSize <= 14) and (VirtualSize2 > 14) and (NumberOfSections <= 4.5) and (ExportSize <= 138.5) and (ImageVersion > 1005) => isDirty = 1  (37.0/0.0) [17.0/0.0]
	elif input.DebugSize <= 14 and input.VirtualSize2 > 14 and input.NumberOfSections > 4.5 and input.ExportSize > 138.5 and input.ImageVersion > 1005:
		isDirty = 1
#Except (ImageVersion <= 5005) and (DebugSize <= 14) and (VirtualSize2 > 14) and (NumberOfSections <= 4.5) => isDirty = 1  (182.0/20.0) [88.0/6.0]
	elif input.ImageVersion <= 5005 and input.DebugSize <= 14 and input.VirtualSize2 > 14 and input.NumberOfSections <= 4.5:
		isDirty = 1
#Except (ImageVersion <= 5005) and (DebugSize <= 14) and (ImageVersion <= 5) and (NumberOfSections > 3.5) and (ExportSize <= 164.5) and (IatRVA <= 73728) and (ResourceSize <= 8722) => isDirty = 1  (47.0/0.0) [18.0/2.0]
	elif input.ImageVersion <= 5005 and input.DebugSize <= 14 and input.ImageVersion <=5 and input.NumberOfSections > 3.5 and input.ExportSize <= 164.5 and input.IatRVA <= 73728 and input.ResourceSize <= 8722:
		isDirty = 1
#Except (ImageVersion <= 5005) and (DebugSize <= 14) and (ResourceSize > 21108) and (ResourceSize <= 37272) and (ImageVersion <= 760) => isDirty = 1  (51.0/0.0) [30.0/3.0]
	elif input.ImageVersion <= 5005 and input.DebugSize <= 14 and input.ResourceSize > 21108 and input.ResourceSize <= 37272 and input.ImageVersion <= 760:
		isDirty = 1
#Except (NumberOfSections > 4.5) and (ExportSize <= 25.5) and (ImageVersion > 1505) and (ResourceSize <= 1020) => isDirty = 1  (51.0/0.0) [30.0/2.0]
	elif input.NumberOfSections > 4.5 and input.ExportSize <= 25.5 and input.ImageVersion > 1505 and input.ResourceSize <= 1020:
		isDirty = 1
# Except (ImageVersion <= 1500) and (NumberOfSections > 5.5) and (ExportSize <= 101) and (ResourceSize <= 3168) => isDirty = 1  (16.0/0.0) [8.0/1.0]
	elif input.ImageVersion <= 1500 and input.NumberOfSections > 5.5 and input.ExportSize <= 101 and input.ResourceSize <= 3168:
		isDirty = 1
#Except (ImageVersion <= 3025) and (DebugSize <= 14) and (ResourceSize > 1182) and (VirtualSize2 > 164) and (ExportSize <= 330.5) => isDirty = 1  (32.0/7.0) [20.0/4.0]
	elif input.ImageVersion <= 3025 and input.DebugSize <= 14 and input.ResourceSize > 1182 and input.VirtualSize2 > 164 and input.ExportSize <= 330.5:
		isDirty = 1
# Except (ImageVersion <= 1010) and (ResourceSize > 2352) and (VirtualSize2 > 39914) and (VirtualSize2 <= 153258) and (VirtualSize2 > 115254) => isDirty = 1  (19.0/0.0) [8.0/2.0]
	elif input.ImageVersion <= 1010 and input.ResourceSize > 2352 and input.VirtualSize2 > 115254 and input.VirtualSize2 <= 153258:
		isDirty = 1
#Except (ImageVersion <= 1500) and (NumberOfSections > 5.5) and (ImageVersion <= 500) and (ExportSize <= 164) and (IatRVA <= 2048) => isDirty = 1  (7.0/0.0) [3.0/0.0]
	elif input.ImageVersion <= 1500 and input.NumberOfSections > 5.5 and input.ImageVersion <= 500 and input.ExportSize <= 164 and input.IatRVA <= 2048:
		isDirty = 1
# Except (ImageVersion <= 1010) and (ResourceSize <= 474) and (IatRVA > 26624) and (VirtualSize2 > 1802) and (IatRVA <= 221348) => isDirty = 1  (15.0/0.0) [5.0/2.0]
	elif input.ImageVersion <= 1010 and input.ResourceSize <= 474 and input.IatRVA > 26624 and input.VirtualSize2 > 1802 and input.IatRVA <= 221348:
		isDirty = 1
# Except (ImageVersion <= 2500) and (DebugSize <= 14) and (ResourceSize > 4320) and (ResourceSize <= 389246) and (ResourceSize > 78678) and (NumberOfSections <= 4) and (ResourceSize <= 120928) => isDirty = 1  (7.0/0.0) [3.0/1.0]
	elif input.ImageVersion <= 2500 and input.DebugSize <= 14 and input.ResourceSize > 78678 and input.ResourceSize <= 120928 and input.NumberOfSections <= 4:
		isDirty = 1
# Except (ImageVersion <= 5005) and (ExportSize <= 25.5) and (NumberOfSections > 3.5) and (ResourceSize > 35814) and (VirtualSize2 > 215352) => isDirty = 1  (5.0/0.0) [1.0/0.0]
	elif input.ImageVersion <= 5005 and input.ExportSize <= 25.5 and input.NumberOfSections > 3.5 and input.ResourceSize > 35814 and input.VirtualSize2 > 215352:
		isDirty = 1
# Except (ImageVersion <= 4005) and (IatRVA <= 2560) and (NumberOfSections > 3.5) and (ImageVersion <= 500) and (ResourceSize > 648) and (ResourceSize <= 62291) => isDirty = 1  (9.0/0.0) [4.0/1.0]
	elif input.ImageVersion <= 500 and input.IatRVA <= 2560 and input.NumberOfSections > 3.5 and input.ResourceSize > 648 and input.ResourceSize <= 62291:
		isDirty = 1
# Except (ExportSize <= 25.5) and (NumberOfSections > 4.5) and (VirtualSize2 > 50765) and (ResourceSize <= 741012) and (ResourceSize > 2512) => isDirty = 1  (13.0/0.0) [6.0/0.0]
	elif input.ExportSize <= 25.5 and input.NumberOfSections > 4.5 and input.VirtualSize2 > 50765 and input.ResourceSize <= 741012 and input.ResourceSize > 2512:
		isDirty = 1
# Except (ImageVersion <= 1010) and (ExportSize <= 25.5) and (VirtualSize2 > 63) and (VirtualSize2 <= 3448) and (ResourceSize > 2032) and (VirtualSize2 > 1200) and (VirtualSize2 <= 3278) => isDirty = 1  (7.0/0.0) [4.0/2.0]
	elif input.ImageVersion <= 1010 and input.ExportSize <= 25.5 and input.VirtualSize2 <= 3278 and input.VirtualSize2 > 1200 and input.ResourceSize > 2032:
		isDirty = 1
#Except (ResourceSize <= 474) and (ExportSize <= 76) and (VirtualSize2 <= 1556) and (IatRVA <= 2368) => isDirty = 1  (13.0/0.0) [2.0/0.0]
	elif input.ResourceSize <= 474 and input.ExportSize <= 76 and input.VirtualSize2 <= 1556 and input.IatRVA <= 2368:
		isDirty = 1
# Except (ImageVersion <= 1500) and (VirtualSize2 <= 6) and (IatRVA > 2048) => isDirty = 1  (8.0/0.0) [4.0/1.0]
	elif input.ImageVersion <= 1500 and input.VirtualSize2 <= 6 and input.IatRVA > 2048:
		isDirty = 1
	else:
		isDirty = 0
	return isDirty
 

 
parser = argparse.ArgumentParser(description='Classify an unknown binary as MALWARE or CLEAN.')
#创建解析器对象ArgumentParser，可以添加参数
#add_argument()方法，用来指定程序需要接受的命令参数
parser.add_argument('-f', metavar='filename', help='The name of the input file')
parser.add_argument('-n', metavar='model', help='The ordinal for model classifier: 0=all (default) | 1=J48 | 2=J48Graft | 3=PART | 4=Ridor')
parser.add_argument('-v', nargs='?', metavar='verbose', help='Dump the PE data being processed', const='verbose')
 
args = parser.parse_args()
#parse_args()是将之前add_argument()定义的参数进行赋值，并返回相关的namespace
 
if not args.f:
	parser.print_help()
	sys.exit(0)
 
input = PEFile(args.f)
 
# 所有变量都可作为“input”对象的值访问
if(args.v):
	input.DataDump()
 
# 判断输入的args
if not args.n:
	args.n = 0
args.n = int(args.n)
if args.n < 0 or args.n > 4:
	parser.print_help()
	sys.exit(0)
	
# Options 0: Run all models	
if(args.n == 0):
	if DEBUG:
		print ('Processing all...')
	print ('Processing all...')
	print('luke fingerprint')
	result1 = runJ48()
	result2 = runJ48Graft()
	result3 = runPART()
	result4 = runRidor()
	res1='%d'%result1
	res2='%d'%result2
	res3='%d'%result3
	res4='%d'%result4
	if ((result1 == result2) and (result2 == result3) and (result3 == result4)):
		print ('J48:\t'+res1)
		print ('J48Graft:\t'+res2)
		print ('PART:\t'+res3)
		print ('RIDOR:\t'+res4)
		print('恶意代码:\t'+res1)
	else:
		print ('J48:\t'+res1)
		print ('J48Graft:\t'+res2)
		print ('PART:\t'+res3)
		print ('RIDOR:\t'+res4)
		print('恶意代码:\tUNKNOWN')
	
# Options 1:  Run J48	
if(args.n == 1):
	if DEBUG:
		print ('Processing J48...')
	printResult(runJ48())
	
# Options 2:  Run J48
if(args.n == 2):
	if DEBUG:
		print ('Processing J48Graft...')
	printResult(runJ48Graft())	
	
# Option 3:  Run PART
if(args.n == 3):
	if DEBUG:
		print ('Processing PART...')
	printResult(runPART())
 
# Option 4:  Run Ridor
if(args.n == 4):
	if DEBUG:
		print ('Processing Ridor...')
	printResult(runRidor())
