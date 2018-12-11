source /home/ins-diag-qa/scripts/UTLI/tor_list_stuck.tcl
global tb_dict
set tb_dict {
	TOR5 {ts_IP_sup1 "172.31.236.46" ts_line_sup1 "13" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	      apc_port {"172.31.236.23 1"} psu_cnt "1" card_cfg ""
	     }
        PIDM4 {ts_IP_sup1 "172.31.236.46" ts_line_sup1 "14" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	       apc_port {"172.31.236.23 5 8"} psu_cnt "2" card_cfg "PIPEDREAM"
	      }
        PIDMB5 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "08" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.52 17 18"} psu_cnt "2" card_cfg "PIPEDREAM"
               }
        PIDMB2_CRDC {ts_IP_sup1 "10.124.11.251" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "05" \
                     apc_port {"10.124.11.219 11 12"} psu_cnt "2" card_cfg "PIPEDREAM"
                    }
	BDTN3 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "11" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	       apc_port {"172.31.236.27 13 8"} psu_cnt "2" card_cfg "BODDINGTONS"
	      }
        BDTN4 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "37" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
               apc_port {"172.31.162.31 11" "172.31.162.30 11"} psu_cnt "2" card_cfg "BODDINGTONS"
              }
        BDTN7 {ts_IP_sup1 "172.31.236.43" ts_line_sup1 "03" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
               apc_port {"172.31.236.19 7 13"} psu_cnt "2" card_cfg "BODDINGTONS"
              }
        BDTN8 {ts_IP_sup1 "172.31.236.43" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
               apc_port {"172.31.236.19 8 11"} psu_cnt "2" card_cfg "BODDINGTONS"
              }
 	KRIEK1 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "20" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.23 13 15"} psu_cnt "2" card_cfg "KRIEK"
	       }
 	KRIEK2 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "27" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.78 3 4"} psu_cnt "2" card_cfg "KRIEK"
		}
	HAGN4 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "14" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.53 8" "172.31.236.54 8"} psu_cnt "2" card_cfg "HAGGAN"
		}
	COR001 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "23" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.162.69 4 5"} psu_cnt "2" card_cfg ""
		}
	COR4 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "42" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.162.31 7"} psu_cnt "1" card_cfg ""
		}
    RED3 {ts_IP_sup1 "172.31.236.40" ts_line_sup1 "12" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.14 17 18"} psu_cnt "2" card_cfg ""
		}
    RED4 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "10" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.53 14" "172.31.236.54 14"} psu_cnt "2" card_cfg ""
		}        
    RED5 {ts_IP_sup1 "172.31.236.40" ts_line_sup1 "11" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.14 15 16"} psu_cnt "1" card_cfg ""
		}        
	CAGA2 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "16" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.25 8"} psu_cnt "1" card_cfg ""
		}
	CAGA5 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "08" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.53 16" "172.31.236.54 16"} psu_cnt "2" card_cfg ""
		}
	CAGA6 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "20" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.79 3" "172.31.236.78 2"} psu_cnt "2" card_cfg ""
		}        
	OSLO002 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "15" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.25 20" "172.31.236.24 20"} psu_cnt "2" card_cfg ""
		}
	OSLO4 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "11" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.25 23 22"} psu_cnt "2" card_cfg ""
		}
	OSLO_PLUS1 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "07" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.53 17" "172.31.236.54 17"} psu_cnt "2" card_cfg ""
		}	
	SAPO1 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "08" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.24 17 18"} psu_cnt "1" card_cfg ""
		}
	SAPO004 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "18" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.25 15 11"} psu_cnt "2" card_cfg ""
		}
	SAPO_PLUS1 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "10" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.78 11 12"} psu_cnt "2" card_cfg ""
		}	
	SAPO_PLUS2 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "23" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.82 13 14"} psu_cnt "2" card_cfg ""
		}	
	SAPO_PLUS3 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "25" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.27 15 16"} psu_cnt "2" card_cfg ""
		}	
	SAPO_PLUS4 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "35" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.31 13" "172.31.162.30 13"} psu_cnt "2" card_cfg ""
		}	
	COOR004 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "12" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.27 5 6"} psu_cnt "2" card_cfg ""
		}
	COOR2 {ts_IP_sup1 "172.31.236.46" ts_line_sup1 "08" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.25 9 10"} psu_cnt "2" card_cfg ""
		}
	SOCHI2 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "17" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.26 23 24"} psu_cnt "2" card_cfg ""
		}
	SLKE12 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "08" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.27 19 22"} psu_cnt "2" card_cfg "SOUTHLAKE"
		}
	SVAL1 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "08" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.75 3 4"} psu_cnt "1" card_cfg "SQVALLEY"
		}
	SVAL002 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "12" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.53 11" "172.31.236.54 11"} psu_cnt "2" card_cfg "SQVALLEY"
		}
	SARA002 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "19" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.79 22"} psu_cnt "1" card_cfg "SARAJEVO"
		}
	SARA3 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "43" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.23 12"} psu_cnt "1" card_cfg "SARAJEVO"
		}
	ATWP004 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "17" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.78 23 24"} psu_cnt "2" card_cfg "ANTWERP"
		}
	ATWP002 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.53 19" "172.31.236.54 19"} psu_cnt "2" card_cfg "ANTWERP"
		}
 	ATWP5 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "41" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.31 2"} psu_cnt "1" card_cfg "ANTWERP"
		}
	QI2CR3 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "04" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
        apc_port {"172.31.162.52 21 22"} psu_cnt "2" card_cfg ""
               }
	QZ2CR1 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "20" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.39 18 19"} psu_cnt "2" card_cfg ""
               }
	QZ2XL3 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "07" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.52 19"} psu_cnt "1" card_cfg ""
               }
	NGF1 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "17" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.39 3 4"} psu_cnt "2" card_cfg ""
             }      
	NGF2 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "16" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.39 5 6"} psu_cnt "2" card_cfg ""
             }      
	NGF3 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "34" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.69 22" "172.31.236.17 20"} psu_cnt "2" card_cfg ""
             }      
        QKZK1 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "06" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.236.28 15 16"} psu_cnt "2" card_cfg ""
              }
	NEPT1 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "05" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.39 1 20"} psu_cnt "2" card_cfg ""
              }	
	NEPTCR2 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "xx" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.52 x xx"} psu_cnt "2" card_cfg "" 
                }	
	  QI2XL2 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "12" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.39 13 14"} psu_cnt "2" card_cfg ""
                 }      
	  COLA1 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "11" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.39 15 16"} psu_cnt "2" card_cfg ""
     	}
	  COLA2 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "13" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.39 11 12"} psu_cnt "2" card_cfg ""
     	}
	  COLA21 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "14" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.39 9 10"} psu_cnt "2" card_cfg ""
     	}
	  COLA22 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "15" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.39 7 8"} psu_cnt "2" card_cfg ""
     	}
	  COLA23 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "03" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.162.39 21 22"} psu_cnt "2" card_cfg ""
     	}
	STHM1 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "15" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.12 18" "172.31.236.11 17"} psu_cnt "2" card_cfg "STOCKHOLM"
        }
	STHM004 {ts_IP_sup1 "172.31.236.41" ts_line_sup1 "03" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.162.30 1" "172.31.162.31 1"} psu_cnt "2" card_cfg "STOCKHOLM"
        }
	STHM002 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "11" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.53 12" "172.31.236.54 9"} psu_cnt "2" card_cfg "STOCKHOLM"
        }
	STHM003 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "14" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.11 19 20"} psu_cnt "2" card_cfg "STOCKHOLM"
        }
    NOOK6 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "18" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.20 14 15"} psu_cnt "1" card_cfg "NANOOK"
        }
    NOOK007 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "17" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.19 14 15"} psu_cnt "2" card_cfg "NANOOK"
        }
    NOOK8 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "25" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.162.30 19" "172.31.162.31 19"} psu_cnt "2" card_cfg "NANOOK"
        }
    SVAL3 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "14" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.18 9 13"} psu_cnt "2" card_cfg "SQVALLEY"
        }
    TRPC1 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "13" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.18 18 20"} psu_cnt "2" card_cfg "TURIN"
        }        
    TRPC2 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "30" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.25 3" "172.31.236.23 22"} psu_cnt "2" card_cfg "TURIN"
    }     
    TURIN2 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "22" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.162.31 6"} psu_cnt "1" card_cfg "TURIN"
        }        
    TURIN4 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "06" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.18 7 8"} psu_cnt "2" card_cfg "TURIN"
        }
    TURIN3 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "16" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.18 3 4"} psu_cnt "2" card_cfg "TURIN"
        }
    NOOK21_CRDC {ts_IP_sup1 "10.74.107.2" ts_line_sup1 "03" ts_IP_sup2 "172.21.159." ts_line_sup2 "16" \
        apc_port {"10.74.107.3 15 14"} psu_cnt "2" card_cfg "NANOOK"
    }         
    MABK5 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "06" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.78 17 18"} psu_cnt "2" card_cfg "MAIBOCK"
        }        
    DEVL005 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "09" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.12 15 16"} psu_cnt "1" card_cfg "DEVALLEY"
        }
    DEVL7 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "08" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.236.77 7 8"} psu_cnt "2" card_cfg "DEVALLEY"
        }
    DEVL8 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "29" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
			apc_port {"172.31.162.30 18" "172.31.162.31 18"} psu_cnt "2" card_cfg "DEVALLEY"
        }        
	CHMX7 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "21" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
        apc_port {"172.31.162.31 22" "172.31.162.30 22"} psu_cnt "2" card_cfg "CHAMONIX"
      } 
	CHMX8 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "27" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.236.28 9 10"} psu_cnt "2" card_cfg "CHAMONIX"
      } 
	CHMX9 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "03" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.236.25 4" "172.31.236.23 6"} psu_cnt "2" card_cfg "CHAMONIX"
      }
	CHMX11 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "07" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.236.79 4 5"} psu_cnt "2" card_cfg "CHAMONIX"
      }
	CHMX005 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "02" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.236.76 23 24"} psu_cnt "2" card_cfg "CHAMONIX"
      }
	CHMX006 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "05" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.236.75 11 12"} psu_cnt "2" card_cfg "CHAMONIX"
      }
	HVSU_CR002 {ts_IP_sup1 "172.31.236.81" ts_line_sup1 "15" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.83 20 21"} psu_cnt "2" card_cfg "HAVASU2"
		}      
	HVSU_OE1 {ts_IP_sup1 "172.31.236.41" ts_line_sup1 "16" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.16 11 12"} psu_cnt "2" card_cfg "HAVASU2"
		}      
	HVSU_XR1 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "23" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.30 21" "172.31.162.31 21"} psu_cnt "2" card_cfg "HAVASU2"
		}      
	SMTZ7 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "13" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.76 17 18"} psu_cnt "2" card_cfg "STMORITZ"
		}  
	SMTZ8 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "11" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.77 24 22"} psu_cnt "2" card_cfg "STMORITZ"
		}
	SMTZ9 {ts_IP_sup1 "172.31.236.50" ts_line_sup1 "01" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.65 23 24"} psu_cnt "2" card_cfg "STMORITZ"
		}
	SMTZ10 {ts_IP_sup1 "172.31.236.50" ts_line_sup1 "02" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.65 21 22"} psu_cnt "2" card_cfg "STMORITZ"
		}
	SMTZ006 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "28" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.31 3"} psu_cnt "1" card_cfg "STMORITZ"
		}	
	BLVU007 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "19" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.31 24" "172.31.162.30 14"} psu_cnt "2" card_cfg "BELLEVUE"
		}
	BLVU6 {ts_IP_sup1 "172.31.236.50" ts_line_sup1 "12" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.65 19 20"} psu_cnt "2" card_cfg "BELLEVUE"
		}
	BLVU003 {ts_IP_sup1 "172.31.236.50" ts_line_sup1 "14" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.11 4 8"} psu_cnt "1" card_cfg "BELLEVUE"
		}        
	BLVU004 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "16" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.12 5 11"} psu_cnt "2" card_cfg "BELLEVUE"
		}        
	BLVU5 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.77 19 20"} psu_cnt "2" card_cfg "BELLEVUE"
		}
	BDOG1 {ts_IP_sup1 "172.31.236.41" ts_line_sup1 "14" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.16 2 3"} psu_cnt "2" card_cfg "BREWDOG"
		}
	BDOG2 {ts_IP_sup1 "172.31.236.41" ts_line_sup1 "08" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.16 20" "172.31.162.52 20"} psu_cnt "2" card_cfg "BREWDOG"
		}
	BDOG3 {ts_IP_sup1 "172.31.236.40" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.14 22 23"} psu_cnt "2" card_cfg "BREWDOG"
		}
	BDOG4 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "43" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.90 15 16"} psu_cnt "2" card_cfg "BREWDOG"
		}
	SOPC1 {ts_IP_sup1 "172.31.236.40" ts_line_sup1 "03" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.14 20 21"} psu_cnt "2" card_cfg "SEOUL"
		}
 	SOPC2 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "10" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.19 19 20"} psu_cnt "2" card_cfg "SEOUL"
		}       
 	SEOUL12 {ts_IP_sup1 "172.31.236.44" ts_line_sup1 "18" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.80 1 2"} psu_cnt "2" card_cfg "SEOUL"
		}       
 	SEOUL14 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "09" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.79 11 12"} psu_cnt "2" card_cfg "SEOUL"
		}       
 	SEOUL15 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "23" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.4 17 18"} psu_cnt "2" card_cfg "SEOUL"
		}       
 	SEOUL16 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "24" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.4 19 20"} psu_cnt "2" card_cfg "SEOUL"
		}       
	PARIS1 {ts_IP_sup1 "172.31.236.41" ts_line_sup1 "12" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.16 15 16"} psu_cnt "2" card_cfg "PARIS"
		}
	PARIS002 {ts_IP_sup1 "172.31.236.41" ts_line_sup1 "13" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.16 21 22"} psu_cnt "1" card_cfg "PARIS" 
		}
	PARIS3 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "11" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.20 19 20"} psu_cnt "2" card_cfg "PARIS" 
		}
	PARIS4 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "24" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.78 21 22"} psu_cnt "2" card_cfg "PARIS"
		}        
	PARIS5 {ts_IP_sup1 "172.31.236.41" ts_line_sup1 "17" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.52 23 24"} psu_cnt "2" card_cfg "PARIS"
		}        
	PARIS6 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "15" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.54 24" "172.31.236.53 3"} psu_cnt "2" card_cfg "PARIS"
		}
	PARIS7 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "26" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.31 5" "172.31.162.30 5"} psu_cnt "2" card_cfg "PARIS"
		}
	PARIS8 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "33" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.69 21"} psu_cnt "1" card_cfg "PARIS"
		}
	PARIS1_CRDC {ts_IP_sup1 "10.74.107.2" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"10.74.107.3 20 19"} psu_cnt "2" card_cfg "PARIS"
		}         
    BRLN5 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "17" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
                apc_port {"172.31.236.21 19 20"} psu_cnt "2" card_cfg "BERLIN"
                }
	SLKE8 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "34" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.28 1 2"} psu_cnt "2" card_cfg "SOUTHLAKE"
		}   
	SOCHI_M1 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "13" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.53 10" "172.31.236.54 10"} psu_cnt "2" card_cfg "SOCHI"
		}  
	SOCHI_M3 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "24" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.28 3 4"} psu_cnt "2" card_cfg "SOCHI"
		}        
    LP_M1 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "28" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.66 21 22"} psu_cnt "2" card_cfg "LAKEPLACID"
    }
    LP_M2 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "36" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	apc_port {"172.31.162.31 12" "172.31.162.30 12"} psu_cnt "2" card_cfg "LAKEPLACID"
    }
    LP_M3 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "30" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.26 21"} psu_cnt "1" card_cfg "LAKEPLACID"
    }	
    LP_M5 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "00" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	apc_port {"172.31.162.31 00"} psu_cnt "1" card_cfg "LAKEPLACID"
    }      
    BRLN002 {ts_IP_sup1 "172.31.236.81" ts_line_sup1 "13" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.82 18 24"} psu_cnt "2" card_cfg "BERLIN"
    }	
    BRLN3 {ts_IP_sup1 "172.31.236.44" ts_line_sup1 "17" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.80 20 24"} psu_cnt "2" card_cfg "BERLIN"
    }	
    BRLN4 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "18" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.77 15 16"} psu_cnt "2" card_cfg "BERLIN"
    }
    BRLN6 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "21" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.82 11 12"} psu_cnt "2" card_cfg "BERLIN"
    }
    BRLN7 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "20" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.31 23" "172.31.162.30 23"} psu_cnt "2" card_cfg "BERLIN"
    }	
    BRLN8 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "32" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.69 20"} psu_cnt "1" card_cfg "BERLIN"
    }	
    BRLN1_CRDC {ts_IP_sup1 "10.74.107.2" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
        apc_port {"10.74.107.3 18 17"} psu_cnt "2" card_cfg "BERLIN"
    }
    KSGT1 {ts_IP_sup1 "172.31.236.51" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.12 19 23"} psu_cnt "2" card_cfg "KINGSGATE"
    }	
    KSGT2 {ts_IP_sup1 "172.31.236.51" ts_line_sup1 "06" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.65 17 18"} psu_cnt "2" card_cfg "KINGSGATE"
    }	
    KSGT3 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "24" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.30 20" "172.31.162.31 20"} psu_cnt "2" card_cfg "KINGSGATE"
    }	
    KSGT4 {ts_IP_sup1 "172.31.236.41" ts_line_sup1 "18" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.16 8"} psu_cnt "1" card_cfg "KINGSGATE"
    }
    KSGT6 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.27 1 2"} psu_cnt "2" card_cfg "KINGSGATE"
    }
    KSGT7 {ts_IP_sup1 "172.31.236.51" ts_line_sup1 "03" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.75 15 16"} psu_cnt "2" card_cfg "KINGSGATE"
    }
    KSGT8 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "12" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.12 9 10"} psu_cnt "2" card_cfg "KINGSGATE"
    }
      SMPN10 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "06" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.25 17 18"} psu_cnt "2" card_cfg "SUMPIN"
    }
    SMPN11 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "13" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.26 12 20"} psu_cnt "2" card_cfg "SUMPIN"
    }
    SMPN12 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "32" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.26 17 10"} psu_cnt "2" card_cfg "SUMPIN"
    }
    SMPN7 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "22" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.52 9 10"} psu_cnt "2" card_cfg "SUMPIN"
    }
    SMPN9 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "17" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.4 3 4"} psu_cnt "2" card_cfg "SUMPIN"
    }
    SMPNB1_CRDC {ts_IP_sup1 "10.124.11.251" ts_line_sup1 "02" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"10.124.11.219 1 2"} psu_cnt "2" card_cfg "SUMPIN"
    }
    SMPNB2_CRDC {ts_IP_sup1 "10.124.11.251" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"10.124.11.219 3 4"} psu_cnt "2" card_cfg "SUMPIN"
    }
    VINA3 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "33" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.28 21 22"} psu_cnt "2" card_cfg "VIENNA"
    }
    VINA4 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "26" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.28 5 13"} psu_cnt "2" card_cfg "VIENNA"
    }
    VINA5 {ts_IP_sup1 "172.31.162.63" ts_line_sup1 "03" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.65  15 16"} psu_cnt "2" card_cfg "VIENNA"
    }
    VINA6 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "32" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.31 10" } psu_cnt "1" card_cfg "VIENNA"
    }
    FOST7 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "38" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.23 11 23"} psu_cnt "2" card_cfg "FOSTERS"
    }
    FOST8 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "20" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.17 15"} psu_cnt "1" card_cfg "FOSTERS"
    }
    FOST9 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "21" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.18 2 6"} psu_cnt "2" card_cfg "FOSTERS"
    }    
    FOST10 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "30" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.30 17" "172.31.162.31 17"} psu_cnt "2" card_cfg "FOSTERS"
    }    
    FOST1_CRDC {ts_IP_sup1 "10.74.107.2" ts_line_sup1 "06" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
        apc_port {"10.74.107.3 13 12"} psu_cnt "2" card_cfg "FOSTERS"
    }         
    SHUG6 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "29" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.24 7 8"} psu_cnt "2" card_cfg "SHUGGA"
    }     
    SHUG7 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "37" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.4 6 7"} psu_cnt "2" card_cfg "SHUGGA"
    }     
    SHUG9 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "21" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.4 14 10" } psu_cnt "2" card_cfg "SHUGGA"
    }     
    SHUG12 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "32" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.23 18 24" } psu_cnt "2" card_cfg "SHUGGA"
    }
    SHUG13 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "33" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.162.30 15"  "172.31.162.31 15"} psu_cnt "2" card_cfg "SHUGGA"
    }      
    SHUG14 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "33" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.4 1 2"} psu_cnt "2" card_cfg "SHUGGA"
    }     
    WLKE1 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "27" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.23 14 17"} psu_cnt "2" card_cfg "WESTLAKE"
    }     
    WLKE2 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "28" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.23 16"} psu_cnt "1" card_cfg "WESTLAKE"
    }     
    WLKE10 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "31" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.23 20"} psu_cnt "1" card_cfg "WESTLAKE"
    }     
    WLKE7 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "40" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.30 8" "172.31.162.31 8"} psu_cnt "2" card_cfg "WESTLAKE"
    }     
    WLKE11 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "40" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.4 13 9" } psu_cnt "2" card_cfg "WESTLAKE"
    }     
    WLKE12 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.4 5 8"} psu_cnt "2" card_cfg "WESTLAKE"
    }     
    DPLK4 {ts_IP_sup1 "172.31.236.81" ts_line_sup1 "11" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.83 17 18"} psu_cnt "2" card_cfg "DEEPLAKE"
    }      
    DPLK9 {ts_IP_sup1 "172.31.236.59" ts_line_sup1 "09" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.73 19 20"} psu_cnt "2" card_cfg "DEEPLAKE"
    }
    DPLK8 {ts_IP_sup1 "172.31.236.59" ts_line_sup1 "26" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.73 5 6"} psu_cnt "2" card_cfg "DEEPLAKE"
    }    
    DPBK4 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "20" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.26 14 16"} psu_cnt "2" card_cfg "DOPPELBOCK"
    }     
    DPBK5 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "39" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.30 9" "172.31.162.30 7"} psu_cnt "2" card_cfg "DOPPELBOCK"
    }     
    DPBK6 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "32" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.86 17 21"} psu_cnt "2" card_cfg "DOPPELBOCK"
    } 
    DPBK7 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "03" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.54 20 21"} psu_cnt "2" card_cfg "DOPPELBOCK"
    }     
    DPBK8 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "13" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.24 9 10"} psu_cnt "2" card_cfg "DOPPELBOCK"
    }     
    DPBK9 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "34" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.86 20 22"} psu_cnt "2" card_cfg "DOPPELBOCK"
    }     
    DPBK10 {ts_IP_sup1 "172.31.162.63" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.65 11 12"} psu_cnt "2" card_cfg "DOPPELBOCK"
    }     
    DPBK11 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "07" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.17 3 4"} psu_cnt "2" card_cfg "DOPPELBOCK"
    }
    SCSW8 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "38" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.30 10" "172.31.162.31 9"} psu_cnt "2" card_cfg "SCRIMSHAW"
    }
    PIDM1 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "19" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.13 14 15"} psu_cnt "2" card_cfg "PIPEDREAM"
    }        
    SCSW12 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "07" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.24 1 2"} psu_cnt "2" card_cfg "SCRIMSHAW"
    }  
    SLKE11 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "13" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.11 12 13"} psu_cnt "2" card_cfg "SOUTHLAKE"
    } 
    TTLY10 {ts_IP_sup1 "172.31.236.81" ts_line_sup1 "02" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.83 9 10"} psu_cnt "2" card_cfg "TETLEY"
    }     
    TTLY11 {ts_IP_sup1 "172.31.162.63" ts_line_sup1 "09" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.27 9 10"} psu_cnt "2" card_cfg "TETLEY"
    }
    TTLY12 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "43" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.30 3 6"} psu_cnt "2" card_cfg "TETLEY"
    }
    TTLY14 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "32" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.14 14 19"} psu_cnt "2" card_cfg "TETLEY"
    }     
    BFST8 {ts_IP_sup1 "172.31.162.63" ts_line_sup1 "08" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.11 10 11"} psu_cnt "2" card_cfg "BIFROST"
    }     
    BFST4 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "18" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.53 21" "172.31.236.54 23"} psu_cnt "2" card_cfg "BIFROST"
    }     
    BFST5 {ts_IP_sup1 "172.31.236.44" ts_line_sup1 "30" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.15 15 20"} psu_cnt "2" card_cfg "BIFROST"
    }     
    BFST9 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "23" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.17 14" "172.31.162.69 9"} psu_cnt "2" card_cfg "BIFROST"
    }     
    SPUP5 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "07" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
    apc_port {"172.31.236.17 13 18"} psu_cnt "2" card_cfg "SHADOWPUPPET"
    }
    SPUP6 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "08" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
    apc_port {"172.31.236.17 21 22"} psu_cnt "2" card_cfg "SHADOWPUPPET"
    }
    SPUP7 {ts_IP_sup1 "172.31.237.73" ts_line_sup1 "07" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
    apc_port {"172.31.237.68 3 12"} psu_cnt "2" card_cfg "SHADOWPUPPET"
    }
    SPUP8 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "34" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
     apc_port {"172.31.162.31 14"} psu_cnt "1" card_cfg "SHADOWPUPPET"
    }
    PIDM2 {ts_IP_sup1 "172.31.236.41" ts_line_sup1 "10" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.17 7 8"} psu_cnt "2" card_cfg "PIPEDREAM"
    }
    SCSW9 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "01" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.11 16 21"} psu_cnt "2" card_cfg "SCRIMSHAW"
    }     
    SCSW10 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "15" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.18 10 14"} psu_cnt "2" card_cfg "SCRIMSHAW"
    }     
    SCSW13 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "07" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.66 16" "172.31.236.28 12"} psu_cnt "2" card_cfg "SCRIMSHAW"
    }     
    MABK7 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "06" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
     apc_port {"172.31.236.12 13 14"} psu_cnt "2" card_cfg "MAIBOCK"
    }     
    MABK9 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "39" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
     apc_port {"172.31.236.25 21 24"} psu_cnt "2" card_cfg "MAIBOCK"
    }     
    MABK8 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "15" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
     apc_port {"172.31.236.79 13 20"} psu_cnt "2" card_cfg "MAIBOCK"
    }    
    MABK4 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "44" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
     apc_port {"172.31.236.53 13" "172.31.236.54 13"} psu_cnt "2" card_cfg "MAIBOCK"
    }    
    MABK6 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "10" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
     apc_port {"172.31.236.75 5 6"} psu_cnt "2" card_cfg "MAIBOCK"
    }    
    RDCT2 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "19" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.66 13 14"} psu_cnt "1" card_cfg "REDCASTLE"
    }     
    RDCT3 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "33" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.69 7 8"} psu_cnt "2" card_cfg "REDCASTLE"
    }     
    RDCT4 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "21" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.53 4" "172.31.236.54 4"} psu_cnt "2" card_cfg "REDCASTLE"
    }     
    HAGN9 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "12" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.78 19 20"} psu_cnt "2" card_cfg "HAGGAN"
    }     
    HAGN2 {ts_IP_sup1 "172.31.236.44" ts_line_sup1 "20" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.80 22 23"} psu_cnt "2" card_cfg "HAGGAN"
    }     
    HAGN3 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "41" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.25 2 7"} psu_cnt "2" card_cfg "HAGGAN"
    }
    HAGN8 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "45" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
     apc_port {"172.31.236.53 7" "172.31.236.54 6"} psu_cnt "2" card_cfg "HAGGAN"
    }    
    HAGN7 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
     apc_port {"172.31.236.75 10 18"} psu_cnt "2" card_cfg "HAGGAN"
    }    
    HAGN10 {ts_IP_sup1 "172.31.162.91" ts_line_sup1 "03" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.82 17 19"} psu_cnt "2" card_cfg "HAGGAN"
    }     
    HAKM1 {ts_IP_sup1 "172.31.237.57" ts_line_sup1 "06" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.237.56 6 16"} psu_cnt "2" card_cfg "HAKIM"
    }     
    HAKM2 {ts_IP_sup1 "172.31.237.57" ts_line_sup1 "03" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.237.56 12 23"} psu_cnt "2" card_cfg "HAKIM"
    }     
    UTPS3 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "41" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.22 19 20"} psu_cnt "2" card_cfg "UTOPIAS"
    }     
    UTPS4 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "28" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.79 6 7"} psu_cnt "2" card_cfg "UTOPIAS"
    }     
    UTPS5 {ts_IP_sup1 "172.31.236.44" ts_line_sup1 "26" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.56 19 20"} psu_cnt "2" card_cfg "UTOPIAS"
    }     
    UTPS6 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "49" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.90 11 13"} psu_cnt "2" card_cfg "UTOPIAS"
    }     
    ELYS1 {ts_IP_sup1 "172.31.237.57" ts_line_sup1 "16" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.237.56 5 10"} psu_cnt "2" card_cfg "ELYSIAN"
    }     
    ELYS2 {ts_IP_sup1 "172.31.237.41" ts_line_sup1 "12" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.237.51 7 12"} psu_cnt "2" card_cfg "ELYSIAN"
    }     
    ELYS3 {ts_IP_sup1 "172.31.237.46" ts_line_sup1 "16" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.237.13 21 22"} psu_cnt "2" card_cfg "ELYSIAN"
    }     
    ELYS4 {ts_IP_sup1 "172.31.237.57" ts_line_sup1 "18" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.237.56 4 18"} psu_cnt "2" card_cfg "ELYSIAN"
    }     
    TRUMER1 {ts_IP_sup1 "173.100.236.49" ts_line_sup1 "09" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {" 172.31.237.x 3"} psu_cnt "1" card_cfg "TRUMER"
    }
    CMRK1 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "44" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.90 2 7"} psu_cnt "2" card_cfg "CHIMNEYROCK"
    }
    CMRK3 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "46" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.90 4 5"} psu_cnt "2" card_cfg "CHIMNEYROCK"
    }
    CMRK4 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "21" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.90 21 22"} psu_cnt "2" card_cfg "CHIMNEYROCK"
    }
    CMRK5 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "20" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.90 19 20"} psu_cnt "2" card_cfg "CHIMNEYROCK"
    }
    CMRK6 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "19" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.90 9 14"} psu_cnt "2" card_cfg "CHIMNEYROCK"
    }
    CMRK7 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "22" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.22 6 21"} psu_cnt "2" card_cfg "CHIMNEYROCK"
    }
    GRLD2 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "26" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.20 24"} psu_cnt "1" card_cfg "GRACELAND"
    }
    GRLD3 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "45" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.90 17"} psu_cnt "1" card_cfg "GRACELAND"
    }
    GRLD4 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "48" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.162.90 24"} psu_cnt "1" card_cfg "GRACELAND"
    }
    SCLP1 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "30" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.82 22" "172.31.236.83 7"} psu_cnt "2" card_cfg "SCULPIN"
    }
    SCLP2 {ts_IP_sup1 "172.31.162.91" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.82 15 16"} psu_cnt "2" card_cfg "SCULPIN"
    }
}





#######################
#this is for chassis that are not running atm or retired
#just for future reference if necessary
####################
set tb_dict_nrunning {
        NA_PIDMB1_CRDC {ts_IP_sup1 "10.124.11.251" ts_line_sup1 "03" ts_IP_sup2 "172.21.159" ts_line_sup2 "05" \
                     apc_port {"10.124.11.219 7 8"} psu_cnt "2" card_cfg "PIPEDREAM"
                    }
	NA_TOR3 {ts_IP_sup1 "172.31.236.466" ts_line_sup1 "01" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.23 1 4"} psu_cnt "1" card_cfg ""
	}
        NA_BDTN5 {ts_IP_sup1 "172.31.236.40" ts_line_sup1 "08" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
               apc_port {"172.31.162.50 15 16"} psu_cnt "2" card_cfg "BODDINGTONS"
              }
	NA_BDTN6 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "09" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.23 3 7"} psu_cnt "2" card_cfg "BODDINGTONS"
	}
	NA_NAGN_M4 {ts_IP_sup1 "172.31.236.46" ts_line_sup1 "10" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.23 9 12"} psu_cnt "2" card_cfg "NAGANO"
	}
	NA_LP_M4 {ts_IP_sup1 "172.31.236.46" ts_line_sup1 "04" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.25 1 2"} psu_cnt "2" card_cfg "LAKEPLACID"
	}
	NA_SOCHI1 {ts_IP_sup1 "172.31.236.46" ts_line_sup1 "16" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.24 9 10"} psu_cnt "2" card_cfg ""
	}
	NA_SOCHI004 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "13" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.27 13 14"} psu_cnt "2" card_cfg ""
	}
	NA_SOCHI_M2 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "23" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.26 1 4"} psu_cnt "2" card_cfg "SOCHI"
		}
	NA_COR2 {ts_IP_sup1 "172.31.236.40" ts_line_sup1 "10" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.13 19 20"} psu_cnt "1" card_cfg ""
	}
	NA_COR3 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "09" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.53 15" "172.31.236.54 15"} psu_cnt "2" card_cfg ""
	}
	NA_COR5 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "02" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.75 17"} psu_cnt "1" card_cfg ""
	}
	NA_RED2 {ts_IP_sup1 "172.31.236.40" ts_line_sup1 "11" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.14 X X"} psu_cnt "1" card_cfg ""
	}
	NA_LIHM1 {ts_IP_sup1 "172.31.236.46" ts_line_sup1 "12" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.24 15 16"} psu_cnt "2" card_cfg ""
	}
	NA_OSLO5 {ts_IP_sup1 "172.31.237.41" ts_line_sup1 "02" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.237.51 6 7"} psu_cnt "2" card_cfg ""
	}
	NA_OSLO_TEST1 {ts_IP_sup1 "172.31.237.85" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.237.84 12 13"} psu_cnt "2" card_cfg ""
	}	
	NA_OSLO_TEST2 {ts_IP_sup1 "172.31.237.85" ts_line_sup1 "06" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.237.84 10 11"} psu_cnt "2" card_cfg ""
	}	        
	NA_SAPO002 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "06" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.23 21 22"} psu_cnt "2" card_cfg ""
	}
	NA_COOR003 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.25 5 6"} psu_cnt "2" card_cfg ""
	}
	NA_MSHT1 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "08" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.21 10 13"} psu_cnt "2" card_cfg ""
	}
	NA_MSHT002 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "14" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.24 19 21"} psu_cnt "2" card_cfg ""
	}
	NA_MSHT5 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "10" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.22 14" "172.31.236.20 13"} psu_cnt "2" card_cfg ""
	}
	NA_PERO1 {ts_IP_sup1 "172.31.236.49" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.28 X X"} psu_cnt "2" card_cfg ""
	}
	NA_HVSU1 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "03" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.28 7 8"} psu_cnt "2" card_cfg "HAVASU"
	}
	NA_HVSU3 {ts_IP_sup1 "172.31.236.46" ts_line_sup1 "03" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.24 11 12"} psu_cnt "2" card_cfg "HAVASU"
	}
	NA_HVSU004 {ts_IP_sup1 "172.31.236.46" ts_line_sup1 "15" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.25 13 19"} psu_cnt "2" card_cfg "HAVASU"
	}
	NA_HVSU005 {ts_IP_sup1 "172.31.236.46" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.25 1 2"} psu_cnt "2" card_cfg "HAVASU"
	}        
	NA_HVSU006 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "14" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.86 21 22"} psu_cnt "2" card_cfg "HAVASU"
	} 
	NA_HVSU007 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "13" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.86 19 20"} psu_cnt "2" card_cfg "HAVASU"
	}
	NA_HVSUB1 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "09" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.27 11 12"} psu_cnt "1" card_cfg "HAVASU2"
	}
	NA_SARA1 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "06" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.53 18" "172.31.236.54 18"} psu_cnt "2" card_cfg "SARAJEVO"
	}
	NA_ATWP1 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "16" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.79 17 18"} psu_cnt "2" card_cfg "ANTWERP"
	}
	NA_ATWP3 {ts_IP_sup1 "172.31.162.63" ts_line_sup1 "10" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.28 17 18"} psu_cnt "2" card_cfg "ANTWERP"
	}        
	NA_QI2CR1 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "04" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
		apc_port {"172.31.236.27 17 18"} psu_cnt "2" card_cfg ""
      }
      NA_QI2CR2 {ts_IP_sup1 "172.31.236.235" ts_line_sup1 "13" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	      apc_port {"172.21.197.83 3 5"} psu_cnt "2" card_cfg ""
      }
      NA_QI2XL1 {ts_IP_sup1 "172.31.237.48" ts_line_sup1 "20" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	      apc_port {"172.31.237.117 9"} psu_cnt "2" card_cfg ""
      }
      NA_BANF1 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "10" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	      apc_port {"172.31.236.78 16 14"} psu_cnt "2" card_cfg ""
}
NA_SLC1 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "09" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.236.78 X X"} psu_cnt "2" card_cfg ""
}  
NA_SLC2 {ts_IP_sup1 "172.31.237.70" ts_line_sup1 "04" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.237.78 X X"} psu_cnt "2" card_cfg ""
}      
NA_NOOK4 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "12" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.236.17 13 14"} psu_cnt "2" card_cfg "NANOOK"
}
NA_NOOK005 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "06" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.236.17 11 12"} psu_cnt "2" card_cfg "NANOOK"
}
NA_NOOK100 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "16" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.236.18 X X"} psu_cnt "2" card_cfg "NANOOK"
}
NA_NOOK102 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "15" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.236.18 X X"} psu_cnt "2" card_cfg "NANOOK"
}
NA_NOOK200 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "08" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.236.17 21 22"} psu_cnt "2" card_cfg "NANOOK"
}        
NA_NOOK201 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "07" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.236.18 18 20"} psu_cnt "2" card_cfg "NANOOK"
}        
NA_DEVL1 {ts_IP_sup1 "172.31.236.70" ts_line_sup1 "14" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.236.77 X" "172.31.236.86 X"} psu_cnt "2" card_cfg "DEVALLEY"
}        
NA_DEVL5 {ts_IP_sup1 "172.31.237.40" ts_line_sup1 "05" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.237.54 9"} psu_cnt "2" card_cfg "DEVALLEY"
}        
NA_DEVL2 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "16" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.236.12 X X"} psu_cnt "2" card_cfg "DEVALLEY"
}        
NA_DEVL4 {ts_IP_sup1 "172.31.236.81" ts_line_sup1 "13" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.236.82 X X"} psu_cnt "2" card_cfg "DEVALLEY"
}        
NA_DEVL3 {ts_IP_sup1 "172.31.236.81" ts_line_sup1 "12" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.236.82 X X"} psu_cnt "2" card_cfg "DEVALLEY"
}
NA_DEVLN {ts_IP_sup1 "172.31.237.40" ts_line_sup1 "03" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	apc_port {"172.31.237.54 4"} psu_cnt "1" card_cfg "DEVALLEY"
    }
    NA_DEVL444 {ts_IP_sup1 "172.31.237.40" ts_line_sup1 "04" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	    apc_port {"172.31.237.54 5"} psu_cnt "1" card_cfg "DEVALLEY"
    }    
    NA_CHMX002 {ts_IP_sup1 "172.31.236.X" ts_line_sup1 "24" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	    apc_port {"172.31.236.X 7 8"} psu_cnt "2" card_cfg "CHAMONIX"
      } 
      NA_CHMX004 {ts_IP_sup1 "172.31.236.81" ts_line_sup1 "14" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	      apc_port {"172.31.236.84 15 16"} psu_cnt "1" card_cfg "CHAMONIX"
      }
      NA_CHMX_MDVT {ts_IP_sup1 "172.31.236.46" ts_line_sup1 "01" ts_IP_sup2 "172.21.159." ts_line_sup2 "05" \
	      apc_port {"172.31.236.24 9 10"} psu_cnt "2" card_cfg "CHAMONIX"
      }
      NA_SMTZ5 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "31" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	      apc_port {"172.31.236.28 13 14"} psu_cnt "2" card_cfg "STMORITZ"
	}
	NA_SEOUL2 {ts_IP_sup1 "172.31.237.45" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.237.55 18 20"} psu_cnt "2" card_cfg "SEOUL"
	}
	NA_SEOUL005 {ts_IP_sup1 "172.31.236.41" ts_line_sup1 "18" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.16 X X"} psu_cnt "2" card_cfg "SEOUL"
	}
 	NA_SEOUL10 {ts_IP_sup1 "172.31.236.71" ts_line_sup1 "13" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.21 1 2"} psu_cnt "2" card_cfg "SEOUL"
		}       
	NA_SEOUL11 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "27" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.162.31 4"} psu_cnt "1" card_cfg "SEOUL"
	}       
	NA_SEOUL13 {ts_IP_sup1 "172.31.236.87" ts_line_sup1 "09" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.86 11 12"} psu_cnt "2" card_cfg "SEOUL"
	}       
	NA_SEOUL17 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "25" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.4 21 22"} psu_cnt "2" card_cfg "SEOUL"
	}       
	NA_SEOUL18 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "26" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.4 23 24"} psu_cnt "2" card_cfg "SEOUL"
	}
	NA_BRLN1 {ts_IP_sup1 "172.31.236.81" ts_line_sup1 "12" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
		apc_port {"172.31.236.82 22 23"} psu_cnt "1" card_cfg "BERLIN"
    }	
    NA_KSGT5 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "12" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.24 13 6"} psu_cnt "2" card_cfg "KINGSGATE"
    }
    NA_SMPN1 {ts_IP_sup1 "172.31.236.48" ts_line_sup1 "32" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.26 X X"} psu_cnt "2" card_cfg "SUMPIN"
    }
    NA_SMPN8 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "31" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.162.30 16" "172.31.162.31 16"} psu_cnt "2" card_cfg "SUMPIN"
    }
    NA_SMPN4 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "23" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.162.52 11 12"} psu_cnt "2" card_cfg "SUMPIN"
    }
    NA_FOST4 {ts_IP_sup1 "172.31.162.63" ts_line_sup1 "09" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.162.66 23 24"} psu_cnt "2" card_cfg "FOSTERS"
    }    
    NA_FOST5 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "11" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
    apc_port {"172.31.236.17 6 12"} psu_cnt "1" card_cfg "FOSTERS"
    }    
    NA_FOST6 {ts_IP_sup1 "172.31.236.85" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.53 22" "172.31.236.54 22"} psu_cnt "2" card_cfg "FOSTERS"
    }    
    NA_FOST11 {ts_IP_sup1 "172.31.237.41" ts_line_sup1 "08" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.237.51 1 2"} psu_cnt "2" card_cfg "FOSTERS"
    }    
    NA_SHUG1 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "07" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.24 17 18"} psu_cnt "2" card_cfg "SHUGGA"
    } 
    NA_SHUG2 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "19" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.24 7 8"} psu_cnt "2" card_cfg "SHUGGA"
    }
    NA_SHUG3 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.28 17 18"} psu_cnt "2" card_cfg "SHUGGA"
    }
    NA_SHUG4 {ts_IP_sup1 "172.31.236.60" ts_line_sup1 "02" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.26 14 15"} psu_cnt "2" card_cfg "SHUGGA"
    }     
    NA_SHUG10 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "22" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.4 15 11" } psu_cnt "2" card_cfg "SHUGGA"
    }     
    NA_SHUG11 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "34" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.4 16 12" } psu_cnt "2" card_cfg "SHUGGA"
    }  
    NA_WLKE5 {ts_IP_sup1 "172.31.236.47" ts_line_sup1 "04" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.4 8"} psu_cnt "1" card_cfg "WESTLAKE"
    }     
    NA_WLKE6 {ts_IP_sup1 "172.31.236.x" ts_line_sup1 "x" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.x 8"} psu_cnt "1" card_cfg "WESTLAKE"
    }     
    NA_DPLK1 {ts_IP_sup1 "172.31.237.42" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.237.56 7 13"} psu_cnt "2" card_cfg "DEEPLAKE"
    }     
    NA_DPLK2 {ts_IP_sup1 "172.31.237.42" ts_line_sup1 "14" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.237.56 10 11"} psu_cnt "2" card_cfg "DEEPLAKE"
    }
    NA_DPLK6 {ts_IP_sup1 "172.31.236.59" ts_line_sup1 "12" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.73 7 8"} psu_cnt "2" card_cfg "DEEPLAKE"
    }
    NA_PIWK {ts_IP_sup1 "172.31.162.xx" ts_line_sup1 "xx" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.162.52 x x"} psu_cnt "2" card_cfg "PIPEWORK"
    }     
    NA_PIDM3 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "xx" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.236.13 x x"} psu_cnt "2" card_cfg "PIPEDREAM"
    }
    NA_BFST7 {ts_IP_sup1 "172.31.237.41" ts_line_sup1 "05" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.237.51 21"} psu_cnt "1" card_cfg "BIFROST"
    }
    NA_RDCT1 {ts_IP_sup1 "172.31.236.42" ts_line_sup1 "12" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.162.69 1 2"} psu_cnt "2" card_cfg "REDCASTLE"
    }     
    NA_UTPS1 {ts_IP_sup1 "172.31.236.x" ts_line_sup1 "08" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {"172.31.162.x 16 24"} psu_cnt "2" card_cfg "UTOPIAS"
    }     
    NA_CT700 {ts_IP_sup1 "173.100.236.49" ts_line_sup1 "09" ts_IP_sup2 "172.21.159" ts_line_sup2 "16" \
	    apc_port {" 172.31.237.x 3"} psu_cnt "1" card_cfg ""
    }
}

###############################
#
#




# Initialize the known Issue varible
#send_user "\ndiagqa01torlist: $diagqa01torlist\n"
foreach chassis $diagqa01torlist {
    dict append known_hw $chassis {* Known_hw_issue: NONE}
}
# Update known issue for each chassis
set known_hw [ dict replace $known_hw SAMPLE1 {* Known_hw_issue: HAVASU x THKPROXY:THK_TRF_40G
* Known_hw_issue: HAVASU x THKPROXY:THK_TRF_100G
* Known_hw_issue: HAVASU x THKPROXY:PRBS} \
     SLKE8 {* Known_hw_issue: SOUTHLAKE x HEAVENLY:AVS_CHECK
* Known_hw_issue: SOUTHLAKE x HEAVENLY:PRBS} \
     SLKE11 {* Known_hw_issue: SOUTHLAKE x HEAVENLY:AVS_CHECK
* Known_hw_issue: SOUTHLAKE x HEAVENLY:PRBS} \
     SLKE12 {* Known_hw_issue: SOUTHLAKE x HEAVENLY:AVS_CHECK
* Known_hw_issue: SOUTHLAKE x HEAVENLY:PRBS} \
     SCSW8 {* Known_hw_issue: SCRIMSHAW x HEAVENLY:AVS_CHECK
* Known_hw_issue: SCRIMSHAW x HEAVENLY:PRBS} \
     DPLK4 {* Known_hw_issue: DEEPLAKE x HEAVENLY:AVS_CHECK
* Known_hw_issue: DEEPLAKE x HEAVENLY:PRBS} \
     DPLK5 {* Known_hw_issue: DEEPLAKE x HEAVENLY:AVS_CHECK
* Known_hw_issue: DEEPLAKE x HEAVENLY:PRBS} \
     DPLK6 {* Known_hw_issue: DEEPLAKE x HEAVENLY:AVS_CHECK
* Known_hw_issue: DEEPLAKE x HEAVENLY:PRBS} \
     UTPS1 {* Known_hw_issue: UTOPIAS x INNO:I2C
* Known_hw_issue: UTOPIAS x INNO:L2} \
     DPLK8 {* Known_hw_issue: DEEPLAKE x HEAVENLY:AVS_CHECK
* Known_hw_issue: DEEPLAKE x HEAVENLY:PRBS} \
     PARIS002 {* Known_hw_issue: PARIS x PCIE:STRESS} \
     BLVU004 {* Known_hw_issue: BELLEVUE x CPU:PCIE} \
     BLVU007 {* Known_hw_issue: BELLEVUE x CPU:PCIE} \
     BLVU5 {* Known_hw_issue: BELLEVUE x CPU:PCIE} \
     BLVU6 {* Known_hw_issue: BELLEVUE x CPU:PCIE} \
     BLVU003 {* Known_hw_issue: BELLEVUE x CPU:PCIE} \
     PARIS4 {* Known_hw_issue: PARIS x PCIE:STRESS} \
     COR001 {* Known_hw_issue: SELA x ALPINE:PRBS} \
     UTPS3  {* Known_hw_issue: UTOPIAS x DATAPATH:TRF} \
     UTPS4  {* Known_hw_issue: UTOPIAS x DATAPATH:TRF} \
     GRLD2 {* Known_hw_issue: GRACELAND x HOMEWOOD:TRF} \
     SAMPLE2 {* Known_hw_issue: BELLEVUE x CHASSIS:FAN} \
]

## define the tcl stop checking skip list for the  board/chassis
set skip_torTclstp {CAGA5 CHMX11 BFST5 STHM003 DPBK9 UTPS5 ELYS4}

global known_bugs
set known_bugs {\
                {{ATWP} {"TRIDENT MBIST"}} \
                {{HAGN} {"ASICPROXY TD3_MBIST"}} \
                {{DPLK} {"HEAVENLY AVS_CHECK"}} \
                {{SLKE} {"HEAVENLY AVS_CHECK"}} \
                {{SCSW} {"HEAVENLY AVS_CHECK"}} \
                {{DPBK} {"HEAVENLY AVS_CHECK"}} \
                {{NOOK} {"MISC_MPA MPA-MIFPGAINTR"}} \
                {{LP_M} {"MISC_MPA MPA-MIFPGAINTR" "SYSINT"}} \
                {{SARA002} {"TRIDENT"}} \
                {{SOCHI_M1} {"SYSINT" "MISC_MPA"}} \
                {{SOCHI_M3} {"SYSINT TSENS_FAULT_INTR" "SYSINT"}} \
                {{SOCHI_M2} {"SYSINT"}} \
                {{SAPO_PLUS} {"CHASSIS FAN"}} \
                {{SAPO} {"CHASSIS FAN"}} \
                {{OSLO} {"CHASSIS FAN"}} \
                {{SVAL002} {"SYSINT"}} \
                {{SVAL3} {"SYSINT"}} \
                {{NOOK21_CRDC} {"MISC_MPA MPA-MIFPGAINTR"}} \
                {{PARIS4} {"PCIE STRESS"}} \
                {{PARIS002} {"PCIE STRESS"}} \
                {{HVSU_XR1} {"THKPROXY OOBSTAT"}} \
                {{HVSU} {"CHASSIS FAN" "THKPROXY THK_TRF_100G" "THKPROXY THK_TRF_40G"}} \
                {{ALL} {"NONE"}} \
                }


# stop on error request
# CDET system_stop for each chassis
global system_stop
set system_stop {\
                {{ELYS} {"MISC:FPGAINTR"}} \
                {{ATWP} {"TD2PROXY:TIB_TD2_TRF" "TIB:MBIST" "TIB:REGACC" "DONNER:TRF" "DONNER:INT_TRF" "TRIDENT:DIAG_TRF"}} \
                {{NOOK} {"THKPROXY:INT_TRF" "THKPROXY:THK_TRF"}} \
                {{STHM} {"TD2PROXY:PRBS"}} \
                {{COR} {"TRIDENT:INT_TRF"}} \
                {{RDCT1} {"ASICPROXY:CHL_TRF" "ASICPROXY:CHL_PRBS"}} \
                {{RDCT} {"SYSINT:TSENS_FAULT_INTR"}} \
                {{NOOK} {"RESET:PHY_RESET" "THKPROXY:THK_TRF"}} \
                {{BRLN} {"TD2PROXY:PRBS" "TD2PROXY:TR72_TRF"}} \
                {{SLKE8} {"SFP_MGT:PROBE"}} \
                {{TTLY14} {"CHASSIS:PSU"}} \
                {{TTLY9} {"CHASSIS:PSU"}} \
                {{RDCT3} {"SFP_MGT:TRAFFIC"}} \
                {{PARIS1_CRDC} {"MISC:FPGAINTR" "MISC:SSD" "MISC:SSD-RW" "PERF:SSD-BW"}} \
                {{ALL} {"MISC:WDT"}} \
                }


# set boot image on  requestcd 
# system can choose different private image
# change again
# set_private_image_flag = 1 mean using private image. set_private_image_flag = 0 no private image
set set_private_image_flag 1
#set system_imageBoot {
#                    {{ALL} {"/hjiang/8slot/latest/" "diag-sup-x86_64"}}
#                    {{UTPS KRIEK VINA SMPN HAGN MABK SPUP SHUG WLKE FOST DPBK BFST PIDM RDCT SLKE DPLK SCSW TTLY ELYS BDOG CMRK BDTN SCLP} {"/hjiang/8slot/latest/" "yh_tor2"}} 
#                    {{GRLD} {"/hjiang/8slot/hong/" "yh_tor21030201801"}}
#}
# set system_imageBoot {
                     # {{DPBK SHUG BFST} {"/hjiang/8slot/latest/" "yh_tor21120"}}
                     # {{SEOUL CHMX} {"/hjiang/8slot/latest/" "yh_sup1120"}}
                     # }
#set system_imageBoot {
#                     {{ALL} {"/hjiang/8slot/latest/" "yh_sup1120"}}
#                     {{GRLD UTPS KRIEK VINA SMPN HAGN MABK SPUP SHUG WLKE FOST DPBK BFST PIDM RDCT SLKE DPLK SCSW TTLY ELYS BDOG BDTN SCLP} {"/hjiang/8slot/latest/" "yh_tor21120"}}
#                     {{CMRK} {"/hjiang/8slot/hong/" "diag-tor2-x86_64-1024201801"}}
#                     }                     

## PIDMB release 
set system_imageBoot {
                      {{UTPS} {"/hjiang/8slot/hong/" "yh_tor2_1205201801"}}
                      {{GRLD} {"/hjiang/8slot/hong/" "yh_tor2_1206201801"}}
                      {{ELYS} {"/hjiang/8slot/hong/" "diag-tor2-x86_64-08062018-1"}}
                      {{ATWP002 TURIN2 SEOUL14 KSGT2} {"/weihozha/" "diag-sup-x86_64"}}
                      {{WLKE11 FOST7 SMPN7 VINA3} {"/weihozha/" "diag-tor2-x86_64"}}
                     }
                     
#                
# set to 1, run test; set to 0, not run
# how many iteration for the whole test
global boot_string 
global test_duration sup_pw pw_enable
#set test_duration 7200-----hong
set test_duration 7200
set sup_pw "ins123diag"
set pw_enable 1
global power_cycle_1st_iteration
set power_cycle_1st_iteration 1
# 0: normal; 1: ORT; 2: P2C; 3: RDT; 4:4C ;  
set mfg_mode 0
set SDK_chassis {ATWP HVSU}
set ASIC_chassis {ATWP BLVU CHMX DEVL SEOUL SMTZ SOPC}
# how many iteration to do either chassis level power cycle or board_reboot
global power
## power = 2 ==> powercycle every 2 iteration
set power 1
global run_cnt
#set run_cnt 200------------------hong default run_cnt change to test number
set run_cnt 500 
set verify_run_cnt 1
set  verify_run_version 0
global board_reboot_flag
set board_reboot_flag 0
global power_cycle_flag
set power_cycle_flag 1

global stop_on_error
set stop_on_error 2                       

# tftpboot: if image under /tftpboot/user, put "/user/" as dir and follow by the file name
global tftp_server
#set tftp_server "172.31.236.30"
set tftp_server "172.31.162.33"
set tftp_server_crdc "10.74.69.38"
set default_gw_crdc "10.74.107.1"
set default_gw_crdc_bma "10.124.11.254"
set netmask_crdc "255.255.255.0"
# clear ip and gw address at loader prompt. 1 is reset ip. 0 is no reset ip.
set clear_ipaddress_flag 1

## PMRO settting
global pmro_sugarbowl pmro_bigsky pmro_homewood pmro_lacross pmro_davos
set pmro_sugarbowl "sys_default"
set pmro_bigsky "sys_default"
set pmro_homewood "sys_default"
set pmro_lacross "sys_default"
set pmro_davos "sys_default"

## Asic
set asic_chip "UNKNOWN"

global tor_dir
#set tor_dir /yanhzhan/8slot/05-23-release/
set tor_dir /hjiang/8slot/latest/
# set tor_dir /hjiang/8slot/tmp1/
global apc_pw
set apc_pw "insieme"
# Image name
global sup_image
set sup_image "yh_sup"
set sup_tip_image "yh_sup"
global mem_flag
set mem_flag 1
# test sequence
global tor_test_sequence
set tor_test_sequence " 1. Run MISC BIOS;\n 2. Run GE;\n 3. Run OBFL;\n 4. Run RESET;\n 5. Run RETIMER;\
						\n 6. Run_on_time with test duration $test_duration secs, with test 1-4 and PERF skipped \n 7. Run PERF \
						\n 8. Repeat with power cycle \
						\n 9. Image used: $tor_dir \
                                                \n\n Fan speed set to 100% of full speed"
global tor_test_sequence_cor
set tor_test_sequence_cor " 1. Run MISC BIOS; \n 2. Run TRIDENT INTERNAL TRAFFIC TEST; \n 3. PREPARE FOR ALPINE LIB; \n 4. Run ALPINE TEST; \
						\n 5. Run GE; \n 6. Run OBFL; \n 7. Run SYSINTR; \n 8. Run PERF; \n 9. Run  MEMTESTER; \n 10. Run the rest in parallel along with TD2 INT_TRF; \
						\n 11. Repeat with power cycle;\
						\n 12. Image used: $tor_dir;\
                                                 \n\n Fan speed set to 100% of full speed"
global tor_test_sequence_red
set tor_test_sequence_red " 1. Run MISC BIOS; \n 2. Run MISC MIFPGAINTR; \n 3. Run GE; \n 4. Run SYSINT;  \n 5. Run PERF ; \
						 \n 6. Run  MISC RED2_PM ; \n 7. Run MEMTESTER; \n 8. Repeat with power cycle; \
                                                 \n 9. Image used: $tor_dir; \
						 \n\n Fan speed set to 100% of full speed"

global miller_test_sequence
set miller_test_sequence " 1. Run_on_time qsfp_mpa misc_mpa with test duration $test_duration secs\n \
						 2. Run Nstar script\n \
						 3. Image used: $tor_dir\n \
						 4. Repeat with power cycle\n"

### test
global ssd_init_flag
set ssd_init_flag 0
global usb_init_flag
set usb_init_flag 0
global remove_OS_flag
set remove_OS_flag 0
global reset_ip_flag
set reset_ip_flag 0
global oldImage_flag 
set oldImage_flag 0

### export ip for reach POE tester
global top_poe_ip top_poe_port bottom_poe_ip bottom_poe_port
set top_poe_ip "172.31.162.38"
set top_poe_port "2018"
set bottom_poe_ip "172.31.162.38"
set bottom_poe_port "2009"

### export ip for reach POE tester(PIDMB5)
global top_poe_PIDMB5_ip top_poe_PIDMB5_port bottom_poe_PIDMB5_ip bottom_poe_PIDMB5_port
set top_poe_PIDMB5_ip "172.31.162.38"
set top_poe_PIDMB5_port "2034"
set bottom_poe_PIDMB5_ip "172.31.162.38"
set bottom_poe_PIDMB5_port "2006"

### export ip for reach POE tester
global top_poe_ip_grld3 top_poe_port_grld3
set top_poe_ip_grld3 "172.31.236.71"
set top_poe_port_grld3 "2047"


### This flag for upgrade M600 ssd firmware
global upgrade_ssd_fw 
set upgrade_ssd_fw 2

# To run bios switching, set dry_run to 1 and bios_sw_flag to 1. 
# set dry_run to 2 is for upgrade SSD firmware
global dry_run bios_sw_flag bios_sw_stop_on_error repeat_iteration
set dry_run 0
set bios_sw_flag 0
set auto_boot_flag 0
set boot_image_flag 0
# use chassis_reboot_flag to reboot/power cycle chassis
set chassis_reboot_flag 0
set bios_sw_stop_on_error 0
set bios_sw_result "" 
# Default have to be 0. If none 0, it will repeatedly run the none 0 that was set
# This feature is for user to set and repeatedly testing the particular iteration 
set repeat_iteration 0

## HVSU_OE setting
## bios_OE_flag == 1 turn on bios programming. bios_OE_flag == 0 is turn off bios programming
global bios_OE_flag repeat_bios_prog bios_oe_path oe_bios n9k_bios
set bios_OE_flag 0
## repeat_bios_prog == 1 to prog bios at every iteration. repeat_bios_prog == 0 only prog bios at 1st and 2nd iteration.
set repeat_bios_prog 0
set bios_oe_path "/home/ins-diag-qa/scripts/TOR/HVSU_OE_Image/"
#set oe_bios "havasu-oe-bios-v120.bin"
set oe_bios "havasu-oe-bios-v130.bin"
#set oe_bios "havasu-oe-bios-v100-02012016-1.bin"
set n9k_bios "first-en-8.23-signed-v2.bin"

## Adaptor test
set adaptor_test 0

global console_flag
set console_flag 0
global oldimage_flag
set oldimage_flag 0
global kill_flag
set kill_flag 0
global usbmount_flag
set usbmount_flag 0
global usbmount_ready_flag
set usbmount_ready_flag 0
global ssdmount_flag
set ssdmount_flag 0
global ssdmount_ready_flag
set ssdmount_ready_flag 0
# if tftpboot_flag=1 means force system boot from tftp server, otherwise ssd drive boot is the first priority. 
# if SSD boot failed, back to tftpboot boot 
set tftpboot_flag 0
set bt_flag 1
global asic_test_flag
set asic_test_flag "100" 
#set asic_test_flag "111"
###############################
#| diag | power | asic | flag |
#+------+-------+------+------+
#|   1  |  0    |   0  | 100  |
#|   1  |  0    |   1  | 101  |
#|   1  |  1    |   1  | 111  |
#|   0  |  0    |   1  | 001  |
#------------------------------ 
set tumx_flag 1
set cli_cmd_flag 1
global test_mode 
set test_mode ""

# set all systems boot from tor2 iamge here
set tor2_systems {SMPN SMPNB VINA FOST SHUG PIWK PIDM PIDMB BFST SPUP BDTN SLKE SCSW WLKE TTLY RDCT DPLK HAGN DPBK \
     MABK KRIEK HAKM UTPS ELYS BDOG CMRK TRUMER GRLD SCLP}
set tor2_fullname_systems {HAGGAN SUMPIN PIPEDREAM PIPEWORK VIENNA FOSTERS SHUGGA WESTLAKE DOPPELBOCK TETLEY BIFROST \
     SHADOWPUPPET BODDINGTONS SCRIMSHAW REDCASTLE DEEPLAKE SOUTHLAKE MAIBOCK KRIEK TSINGTAO HAKIM UTOPIAS ELYSIAN \
     BREWDOG CHYM TRUMER CHIMNEYROCK GRACELAND SCULPIN}

# where do you want to save your log file
global log_dir
set log_dir /vol/diag/logs/ 
set qa_report_dir /home/ins-diag-qa/scripts/
set script_dir /home/ins-diag-qa/scripts/TOR/
# set log_dir /home/ins-diag-qa/
global log_ver_dir
set log_ver_dir /vol/diag/logs/ver_file/ 
set log_torip_dir /vol/diag/logs/torip_file/
set log_shmod /vol/diag/logs/shmod_file/ 
# example set skip_nook "{misc bios} {trident}"
set skip_nook "{MISC USB-RW-EUSB} {PERF EUSB-BW}"
set skip_SMTZ "{PERF USB-BW}"
# set skip_SEOUL ""
set skip_SEOUL "{SUGARBOWL PRBS}"
set skip_SOPC "{SUGARBOWL PRBS}"
set skip_tmp "{RESET PHY_RESET}"
set skip_sval "{MISC USB} {MISC USB-RW-BOTTOM} {MISC USB-RW-TOP}"
set skip_cor "{MISC USB} {MISC USB-RW-BOTTOM} {MISC USB-RW-TOP}"
set skip_red "{MISC USB} {MISC USB-RW-BOTTOM} {MISC USB-RW-TOP}"
set skip_USB "{MISC USB} {MISC USB-RW-BOTTOM} {MISC USB-RW-TOP}"
set skip_osloP "{MISC USB} {MISC USB-RW-BOTTOM} {MISC USB-RW-TOP}"
set skip_caga "{MISC USB} {MISC USB-RW-TOP} {MISC USB-RW-BOTTOM} {PERF USB-BW}"
set skip_devl "{PERF USB-BW}"
set skip_BLVU1 "{CHASSIS FAN}"
set skip_nook1 "{RETIMER} {SFP} {THKPROXY THK_EGL_TRF} {THKPROXY THK_EGL_PRBS} {PERF EUSB-BW} {MISC USB-RW-EUSB} {THKPROXY OOBSTAT}"
############################### Modify history ###################################

# 05.15.2015 Tri: Added SLC info
# 06.04.2015 Adding asic flag
# 06.05.2015 adding skip_nook for Nanook bring up
# 07.07.2015 adding HVSU006 in RDT mode
# 07.10.2015 adding DEVL2 support
# 07.16.2015 adding DEVl3, DEVL4 and DEVL5 support
# 07.17.2015 adding known issue mechanism 
# 08.18.2015 adding known issue DEVL DAVOS:PRBS
# 09.02.2015 Adding devl003 to run 4c
# 11319.2015  added TORM1, TORM2, TORM3 systems in.
# 01.28.2016 update stop on error list.
# 02.09.2016 added SEOUL005 system
# 02.12.2016 added LP_M2 and LP_M3
# 02.23.2016 Fixed miller mifpga variable name
# 03.08.2016 Add BRLN with MISC:USB-RW-TOP error to stop on error
# 03.10.2016 updated programmable version on BERLIN,BELLEVUE,Deer Valley, Chamonix, HVSU_CR.
# 03.25.2016 Adding ASIC and SDK version checking chassis
# 04.01.2016 Added new system BRLN3 and BRLN4
# 04.07.2016 Added new system TURIN1
# 04.13.2016 Cleanup old known issue that not exist anymore.
# 04.14.2016 Update programmable info
# 04.18.2016 TRI: Added SVAL3 P2 board. Mainly for LED test
# 06.01.2016 TRI: Added adaptor_test parameter. 1 enabled, 0 disabled.
# 06.08.2016 TRI: Added programable version for SUMPIN and login info
# 06.20.2016 TRI: Update stop on error for Cdet in wait state. 
# 06.24.1016 TRI: Add new syste BRLN6
# 06.25.2016 TRI: Temp add a skip for SEOUL12 reset phy_reset. Remember to remove this after confirm from DE
# 06.26.2016 TRI: Update stop on error for Cdet in wait state. 
# 06.28.2016 TRI: moved SEOUL12 from 2nd floor lab to first floor lab. Change console and APC.
# 06.29.2016 TRI: Added PARIS6 
# 07.05.2016 TRI: update stop on error for wait cdet.
# 07.06.2016 TRI: Added SEOUL13 and SEOUL14 info
# 07.06.2016 TRI: set know issue on VINE and SMPN on USB test.
# 07.19.2016 TRI: Change NAGN001 to NAGN_M2
# 07.19.2016 TRI: Add VINA2 to run 4C loopback
# 07.20.2016 TRI: Add a new parameter for reseting the ip address at loader prompt. This to clear new system that has 10.x.x.x adress
# 07.25.2016 HOng: Add FOSTERS1 to run p2cx mode. change name from  FOSTER1 to FOST1
# 08.10.2016 TRI: Added FOST2 and FOST3
# 08.17.2016 TRI: Added SMPN2 configure
# 09.08.2016 YH: Added new stop on error test for SMTZ
# 09.14.2016 Hong: updated bios version
# 10.13.2016 Hong: Added FOST7, FOST8 and FOST9
# 10.13.2016 Hong: Added SHUG1 and SHUG2
# 12.06.2016 TRI: Add SHUG8-11 and WLKE4 
# 01.19.2017 TRI: Add WLKE5, SHUG12 and SHUG13
# 01.24.2017 TRI: Add WLKE6 and SMPN9
# 03.09.2017 FAN: Corrected SNPM11 and SMPN12 config info
# 04.05.2017 TRI: Add TETLEY 
# 04.07.2017 TRI: Add PIDM2 
# 04.10.2017 TRI: Add BIFROST
# 05.22.2017 TRI: Replaced BFST1 with BFST2
# 06.09.2017 TRI: Added SDPP1 
# 06.15.2017 YH: Added PIDM iofpga v6
# 06.20.2017 TRI: Change SDPP to SPUP
# 06.20.2017 Hui: Update BIOS version: [NANOOK DEVALLEY CHAMONIX SEOUL TURIN HAVASU2]
# 06.20.2017 Hui: Update IO FPGA version: [NANOOK BIFROST COR DOPPELBOCK HAVASU2]
# 06.20.2017 Hui: Update MI FGPA version: [BIFROST DPBK RED SUMPIN WESTLAKE]
# 06.21.2017 hUI: Update IO FPGA version: [HAVASU2]
# 06.21.2017 Hui: Update MI FGPA version: [DOPPELBOCK TETLEY STMORITZ]
# 06.21.2017 Tri: Add support RedCastle
# 06.21.2017 Hui: Add 'cor_bios_version' as expected BIOS version of COORS
# 06.25.2017 Hui: update BFST FPGA date code
# 07.02.2017 Hui: update MI FPGA0 version: [DPBK]
# 07.02.2017 Hui: update BIOS IO FPGA MI FPGA version: [RDCT]
# 07.14.2017 Tri: Add support for DEEPLAKE and SOUTHLAKE
# 07.17.2017 Hui: update MI FPGA version: [VINA]
# 07.17.2017 Hui: update IO FPGA: [RDCT]
# 07.25.2017 Remove many stop on error per Kevin's request
# 07.25.2017 Hui: update SCSW date code
# 07.26.2017 Hui: update system_stop according to Rui's update
# 08.03.2017 Hui: update BIOS version: [DPBK VINA TTLY SCSW]
# 08.03.2017 Peter: update BIOS version [FOST WLKE PIDM SMPN SHUG]
# 08.08.2017 Tri: Added TTLY4
# 08.10.2017 Hui: update MI FPGA version: [BFST]
# 08.10.2017 Hui: add BIFROST_base_fpga_version REDCASTLE_base_fpga_version to track BASE IO FPGA version
#
