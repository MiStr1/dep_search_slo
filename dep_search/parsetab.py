
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightPLUSrightEQrightSErightDEPOPrightORrightANDrightNEGrightECOMrightTEXTrightXDOTrightBGNrightENDAND ANYTOKEN BGN DEPOP ECOM END EQ LPAR NEG OR PLUS RPAR SE TEXT WORD XDOTsearch : setnodesetnode : BGN setnodesetnode : setnode ENDsetnode : tokendef XDOT setnodesetnode : setnode ECOMsetnode : setnode depresdepres : depnode tokendeftokendef : LPAR setnode RPARdepdef : LPAR depnode RPAR\n              | DEPOPsetnode : tokendefdepnode : depdeftokendef : WORD\n                | TEXT\n                | ANYTOKENdepnode : depnode AND depnodetokendef : tokendef AND tokendeftokendef : tokendef OR tokendefsetnode : setnode PLUS setnodesetnode : setnode EQ setnodesetnode : setnode SE setnodedepnode : depnode OR depnodedepdef : NEG depdeftokendef : NEG tokendef'
    
_lr_action_items = {'BGN':([0,3,5,13,14,15,22,],[3,3,3,3,3,3,3,]),'LPAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,],[5,18,5,-11,5,-13,-14,-15,5,-3,-5,-6,5,5,5,5,-12,18,-10,18,-2,5,5,5,18,-24,-19,-20,-21,-7,18,18,-23,-4,-17,-18,-8,-16,-22,-9,]),'WORD':([0,3,5,9,13,14,15,16,17,19,22,23,24,34,39,40,41,],[6,6,6,6,6,6,6,6,-12,-10,6,6,6,-23,-16,-22,-9,]),'TEXT':([0,3,5,9,13,14,15,16,17,19,22,23,24,34,39,40,41,],[7,7,7,7,7,7,7,7,-12,-10,7,7,7,-23,-16,-22,-9,]),'ANYTOKEN':([0,3,5,9,13,14,15,16,17,19,22,23,24,34,39,40,41,],[8,8,8,8,8,8,8,8,-12,-10,8,8,8,-23,-16,-22,-9,]),'NEG':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,],[9,20,9,-11,9,-13,-14,-15,9,-3,-5,-6,9,9,9,9,-12,20,-10,20,-2,9,9,9,20,-24,20,20,20,-7,20,20,-23,-4,-17,-18,-8,-16,-22,-9,]),'$end':([1,2,4,6,7,8,10,11,12,21,26,27,28,29,30,35,36,37,38,],[0,-1,-11,-13,-14,-15,-3,-5,-6,-2,-24,-19,-20,-21,-7,-4,-17,-18,-8,]),'END':([2,4,6,7,8,10,11,12,21,25,26,27,28,29,30,35,36,37,38,],[10,-11,-13,-14,-15,-3,-5,-6,10,10,-24,10,10,10,-7,10,-17,-18,-8,]),'ECOM':([2,4,6,7,8,10,11,12,21,25,26,27,28,29,30,35,36,37,38,],[11,-11,-13,-14,-15,-3,-5,-6,-2,11,-24,11,11,11,-7,-4,-17,-18,-8,]),'PLUS':([2,4,6,7,8,10,11,12,21,25,26,27,28,29,30,35,36,37,38,],[13,-11,-13,-14,-15,-3,-5,-6,-2,13,-24,13,-20,-21,-7,-4,-17,-18,-8,]),'EQ':([2,4,6,7,8,10,11,12,21,25,26,27,28,29,30,35,36,37,38,],[14,-11,-13,-14,-15,-3,-5,-6,-2,14,-24,14,14,-21,-7,-4,-17,-18,-8,]),'SE':([2,4,6,7,8,10,11,12,21,25,26,27,28,29,30,35,36,37,38,],[15,-11,-13,-14,-15,-3,-5,-6,-2,15,-24,15,15,15,-7,-4,-17,-18,-8,]),'DEPOP':([2,4,6,7,8,10,11,12,18,20,21,25,26,27,28,29,30,31,32,35,36,37,38,],[19,-11,-13,-14,-15,-3,-5,-6,19,19,-2,19,-24,19,19,19,-7,19,19,-4,-17,-18,-8,]),'XDOT':([4,6,7,8,26,36,37,38,],[22,-13,-14,-15,-24,-17,-18,-8,]),'RPAR':([4,6,7,8,10,11,12,17,19,21,25,26,27,28,29,30,33,34,35,36,37,38,39,40,41,],[-11,-13,-14,-15,-3,-5,-6,-12,-10,-2,38,-24,-19,-20,-21,-7,41,-23,-4,-17,-18,-8,-16,-22,-9,]),'AND':([4,6,7,8,16,17,19,26,30,33,34,36,37,38,39,40,41,],[23,-13,-14,-15,31,-12,-10,-24,23,31,-23,23,23,-8,31,31,-9,]),'OR':([4,6,7,8,16,17,19,26,30,33,34,36,37,38,39,40,41,],[24,-13,-14,-15,32,-12,-10,-24,24,32,-23,-17,24,-8,-16,32,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'search':([0,],[1,]),'setnode':([0,3,5,13,14,15,22,],[2,21,25,27,28,29,35,]),'tokendef':([0,3,5,9,13,14,15,16,22,23,24,],[4,4,4,26,4,4,4,30,4,36,37,]),'depres':([2,21,25,27,28,29,35,],[12,12,12,12,12,12,12,]),'depnode':([2,18,21,25,27,28,29,31,32,35,],[16,33,16,16,16,16,16,39,40,16,]),'depdef':([2,18,20,21,25,27,28,29,31,32,35,],[17,17,34,17,17,17,17,17,17,17,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> search","S'",1,None,None,None),
  ('search -> setnode','search',1,'p_top','redone_expr.py',328),
  ('setnode -> BGN setnode','setnode',2,'p_bgn','redone_expr.py',337),
  ('setnode -> setnode END','setnode',2,'p_end','redone_expr.py',342),
  ('setnode -> tokendef XDOT setnode','setnode',3,'p_dot','redone_expr.py',346),
  ('setnode -> setnode ECOM','setnode',2,'p_ecomxpr','redone_expr.py',350),
  ('setnode -> setnode depres','setnode',2,'p_expr2','redone_expr.py',355),
  ('depres -> depnode tokendef','depres',2,'p_sn_depres_a','redone_expr.py',363),
  ('tokendef -> LPAR setnode RPAR','tokendef',3,'p_exprp','redone_expr.py',367),
  ('depdef -> LPAR depnode RPAR','depdef',3,'p_exprp_d','redone_expr.py',376),
  ('depdef -> DEPOP','depdef',1,'p_exprp_d','redone_expr.py',377),
  ('setnode -> tokendef','setnode',1,'p_exprp2','redone_expr.py',384),
  ('depnode -> depdef','depnode',1,'p_exprp5','redone_expr.py',391),
  ('tokendef -> WORD','tokendef',1,'p_exprp3','redone_expr.py',395),
  ('tokendef -> TEXT','tokendef',1,'p_exprp3','redone_expr.py',396),
  ('tokendef -> ANYTOKEN','tokendef',1,'p_exprp3','redone_expr.py',397),
  ('depnode -> depnode AND depnode','depnode',3,'p_dn_and','redone_expr.py',409),
  ('tokendef -> tokendef AND tokendef','tokendef',3,'p_sn_and','redone_expr.py',416),
  ('tokendef -> tokendef OR tokendef','tokendef',3,'p_sn_or','redone_expr.py',420),
  ('setnode -> setnode PLUS setnode','setnode',3,'p_sn_plus','redone_expr.py',424),
  ('setnode -> setnode EQ setnode','setnode',3,'p_sn_eq','redone_expr.py',428),
  ('setnode -> setnode SE setnode','setnode',3,'p_sn_seq','redone_expr.py',432),
  ('depnode -> depnode OR depnode','depnode',3,'p_dn_or','redone_expr.py',436),
  ('depdef -> NEG depdef','depdef',2,'p_dn_not','redone_expr.py',443),
  ('tokendef -> NEG tokendef','tokendef',2,'p_sn_not','redone_expr.py',447),
]
