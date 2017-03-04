import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Leo and Papa!"
line2 = "Ok. Others like mom,dad,nana, other grandparents love him too.."
line3 = "Mr. Wonderful"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
