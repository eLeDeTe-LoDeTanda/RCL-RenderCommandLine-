# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# The Original Code is Copyright (C) 2017 Marcelo "Tanda" Cerviño. http://lodetanda.blogspot.com/ 
# All rights reserved.
#
# Contributor(s):
#
# ***** END GPL LICENCE BLOCK *****

bl_info = {
    "name": "RCL -Render Command Line-",
    "author": "Marcelo 'Tanda' Cerviño",
    "version": (1, 0),
    "blender": (2, 78),
    "location": "Render > RCL -Render Command Line-",
    "description": "RENDER in terminal, IMPORT and EXPORT (executable .sh or .bat) some RENDER OPTIONS",
    "warning": "",
    "wiki_url": "https://github.com/eLeDeTe-LoDeTanda/RCL-RenderCommandLine-",
    "tracker_url": "https://github.com/eLeDeTe-LoDeTanda/RCL-RenderCommandLine-/issues",
    "category": "Render",
}

##################################################################

import bpy

__addon_name__ = "RCL -Render Command Line-"
__url__ = "https://github.com/eLeDeTe-LoDeTanda/RCL-RenderCommandLine-"

class RCLPanel(bpy.types.Panel):
  
    bl_label = __addon_name__
    bl_idname = "RENDER_PT_RCL"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    def draw(self, context):
        layout = self.layout

        blendsaved = os.path.dirname(bpy.data.filepath)

        layout.label(text="-EXPORT render options to FILE:")
        
        if blendsaved:
            row = layout.row()
            row.operator("export.txt", text="Command Line")
            row.operator("export.py", text="Python")
        else: layout.label(text="***Blend file is not saved***")
        
        layout.label(text="-IMPORT render options:")
        row = layout.row()
        row.operator("import.py", text="From Python Script")
        
        layout.label(text="Start render in background:")

        if blendsaved:
            row = layout.row()
            row.scale_y = 3
            row.operator("render.terminal", text="RENDER in Terminal")
        else: layout.label(text="***Blend file is not saved***")

##################################################################

import os
import stat

from bpy_extras.io_utils import ExportHelper, ImportHelper
from bpy.props import StringProperty
from bpy.types import Operator

class ExportCommandLine(Operator, ExportHelper):

    bl_idname = "export.txt"
    bl_label = "Export Render options"

    filename_ext = ".txt"

    filter_glob = StringProperty(
        default="*.txt",
        options={'HIDDEN'},
        maxlen=255, 
        )

    def execute(self, context):
        return write_cl(self.filepath)

      
class ExportPython(Operator, ExportHelper):
    bl_idname = "export.py"
    bl_label = "Export Render options"

    filename_ext = ".py"

    filter_glob = StringProperty(
        default="*.py",
        options={'HIDDEN'},
        maxlen=255, 
        )

    def execute(self, context):
        return write_py(self.filepath)

        
def write_cl(filepath):
    
    Scenename = bpy.context.scene.name
    
    if sys.platform.startswith("win"): 
        file = open(filepath + ".bat", 'w', newline='\r\n', encoding='utf-8')

        file.write(
            "# Auto-generated by " + __addon_name__ + "\n"
            "# " + __url__ + "\n" + "\n"
            "# Command Line:" + "\n" + "\n"
            "call "
            '"' + bpy.app.binary_path + '"' 
            + " -b " + '"' + bpy.data.filepath + '"' 
            + " -S " + Scenename 
            + " -o " + '"' + bpy.data.scenes[Scenename].render.filepath + '"' 
            + " -E %s" % (bpy.data.scenes[Scenename].render.engine) 
            + " -F %s" % (bpy.data.scenes[Scenename].render.image_settings.file_format) 
            + " -x %s" % (int(bpy.data.scenes[Scenename].render.use_file_extension)) 
            + " -t %s" % (bpy.data.scenes[Scenename].render.threads) 
            + " -s %s" % (bpy.data.scenes[Scenename].frame_start) 
            + " -e %s" % (bpy.data.scenes[Scenename].frame_end) 
            + " -j %s" % (bpy.data.scenes[Scenename].frame_step) 
            + " -a"
            )
        
        file.close()
    
        st = os.stat(filepath + ".bat")
        os.chmod(filepath + ".bat", st.st_mode | stat.S_IEXEC)        

    else:  
        file = open(filepath + ".sh", 'w', encoding='utf-8')

        file.write(
            "#!/bin/bash" + "\n" + "\n"
            "# Auto-generated by " + __addon_name__ + "\n"
            "# " + __url__ + "\n" + "\n"
            "# Command Line:" + "\n" + "\n"
            "xterm -e "
            '"' + bpy.app.binary_path + '"' 
            + " -b " + '"' + bpy.data.filepath + '"' 
            + " -S " + Scenename 
            + " -o " + '"' + bpy.data.scenes[Scenename].render.filepath + '"' 
            + " -E %s" % (bpy.data.scenes[Scenename].render.engine) 
            + " -F %s" % (bpy.data.scenes[Scenename].render.image_settings.file_format) 
            + " -x %s" % (int(bpy.data.scenes[Scenename].render.use_file_extension)) 
            + " -t %s" % (bpy.data.scenes[Scenename].render.threads) 
            + " -s %s" % (bpy.data.scenes[Scenename].frame_start) 
            + " -e %s" % (bpy.data.scenes[Scenename].frame_end) 
            + " -j %s" % (bpy.data.scenes[Scenename].frame_step) 
            + " -a"
            )
        
        file.close()
    
        st = os.stat(filepath + ".sh")
        os.chmod(filepath + ".sh", st.st_mode | stat.S_IEXEC)
           
    return {'FINISHED'}


def write_py(filepath):
    
    Scenename = bpy.context.scene.name

    file = open(filepath, 'w', newline='\r\n', encoding='utf-8')
    
    file.write(
        "# Auto-generated by " + __addon_name__ + "\n"
        "# " + __url__ + "\n" + "\n"
        "import bpy" + "\n" + "\n"
        "# Render Options to change" + "\n"
        "############################" + "\n" + "\n" 
        "# Scene Name"+"\n"
        "Scenename = " + '"' + Scenename + '"' + "\n" 
        + "\n"
        "# Render Quality"+"\n"
        "bpy.data.scenes[Scenename].render.resolution_x = %s" 
        % (bpy.data.scenes[Scenename].render.resolution_x) + "\n" 
        "bpy.data.scenes[Scenename].render.resolution_y = %s" 
        % (bpy.data.scenes[Scenename].render.resolution_y) + "\n" 
        "bpy.data.scenes[Scenename].render.resolution_percentage = %s" 
        % (bpy.data.scenes[Scenename].render.resolution_percentage) + "\n"
         
        "bpy.data.scenes[Scenename].render.use_antialiasing = %s" 
        % (bpy.data.scenes[Scenename].render.use_antialiasing) + "\n" 
        "bpy.data.scenes[Scenename].render.antialiasing_samples = " + '"' + "%s" 
        % (bpy.data.scenes[Scenename].render.antialiasing_samples) + '"' + "\n" 
        "bpy.data.scenes[Scenename].render.use_full_sample = %s" 
        % (bpy.data.scenes[Scenename].render.use_full_sample) + "\n" 

        "bpy.data.scenes[Scenename].render.tile_x = %s" 
        % (bpy.data.scenes[Scenename].render.tile_x) + "\n" 
        "bpy.data.scenes[Scenename].render.tile_y = %s" 
        % (bpy.data.scenes[Scenename].render.tile_y) + "\n" 
        "bpy.data.scenes[Scenename].render.threads_mode = " + '"' + "%s" 
        % (bpy.data.scenes[Scenename].render.threads_mode) + '"' + "\n" 
        "bpy.data.scenes[Scenename].render.threads = %s" 
        % (bpy.data.scenes[Scenename].render.threads) + "\n" 
        "bpy.data.scenes[Scenename].render.engine = " + '"' + "%s" 
        % (bpy.data.scenes[Scenename].render.engine) + '"' + "\n" 
        "bpy.data.scenes[Scenename].cycles.samples = %s" 
        % (bpy.data.scenes[Scenename].cycles.samples) + "\n" 
        + "\n"
        "bpy.data.scenes[Scenename].render.dither_intensity = %s" 
        % (bpy.data.scenes[Scenename].render.dither_intensity) + "\n" 
        "bpy.data.scenes[Scenename].render.use_compositing = %s" 
        % (bpy.data.scenes[Scenename].render.use_compositing) + "\n" 
        "bpy.data.scenes[Scenename].render.use_sequencer = %s" 
        % (bpy.data.scenes[Scenename].render.use_sequencer) + "\n" 
        + "\n"

        "# Output"+"\n"
        "bpy.data.scenes[Scenename].render.filepath = " + '"' 
		+ bpy.data.scenes[Scenename].render.filepath + '"' + "\n"
        "bpy.data.scenes[Scenename].render.use_placeholder = %s" 
        % (bpy.data.scenes[Scenename].render.use_placeholder) + "\n" 
        "bpy.data.scenes[Scenename].render.use_overwrite = %s" 
        % (bpy.data.scenes[Scenename].render.use_overwrite) + "\n" 
        "bpy.data.scenes[Scenename].render.image_settings.file_format = " + '"' 
		+ bpy.data.scenes[Scenename].render.image_settings.file_format + '"' + "\n" 
        "bpy.data.scenes[Scenename].render.image_settings.compression = %s" 
        % (bpy.data.scenes[Scenename].render.image_settings.compression) + "\n" 
        "bpy.data.scenes[Scenename].render.image_settings.color_mode = " + '"' 
	    + bpy.data.scenes[Scenename].render.image_settings.color_mode + '"' + "\n" 
        "bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
        % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n" 
        "bpy.data.scenes[Scenename].render.use_file_extension = %s" 
        % (bpy.data.scenes[Scenename].render.use_file_extension) + "\n" 
        "bpy.data.scenes[Scenename].render.use_render_cache = %s" 
        % (bpy.data.scenes[Scenename].render.use_render_cache) + "\n" 
        + "\n"

        "# Stamp"+"\n"
        "bpy.data.scenes[Scenename].render.use_stamp = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp) + "\n" 
        "bpy.data.scenes[Scenename].render.stamp_font_size = %s" 
        % (bpy.data.scenes[Scenename].render.stamp_font_size) + "\n" 
        "bpy.data.scenes[Scenename].render.stamp_background = (%.3f" 
        % (bpy.data.scenes[Scenename].render.stamp_background[0]) 
        + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_background[1])
        + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_background[2])
        + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_background[3]) + ")" + "\n" 
        "bpy.data.scenes[Scenename].render.stamp_foreground = (%.3f" 
	    % (bpy.data.scenes[Scenename].render.stamp_foreground[0])
        + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_foreground[1])
        + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_foreground[2])
        + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_foreground[3]) + ")" + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_labels = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_labels) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_time = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_render_time) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_camera = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_camera) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_date = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_date) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_lens = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_lens) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_render_time = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_render_time) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_filename = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_filename) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_frame = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_frame) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_marker = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_marker) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_scene = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_scene) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_sequencer_strip = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_sequencer_strip) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_note = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_note) + "\n" 
        "bpy.data.scenes[Scenename].render.stamp_note_text = " + '"' 
	    + bpy.data.scenes[Scenename].render.stamp_note_text + '"' + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_memory = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_memory) + "\n" 
        "bpy.data.scenes[Scenename].render.use_stamp_strip_meta = %s" 
        % (bpy.data.scenes[Scenename].render.use_stamp_strip_meta) + "\n" 
        + "\n"

        "# Render frames"+"\n"
        "bpy.data.scenes[Scenename].frame_start = %s" 
        % (bpy.data.scenes[Scenename].frame_start) + "\n" 
        "bpy.data.scenes[Scenename].frame_end = %s" 
        % (bpy.data.scenes[Scenename].frame_end) + "\n" 
        "bpy.data.scenes[Scenename].frame_step = %s" 
        % (bpy.data.scenes[Scenename].frame_step) + "\n" 
        "bpy.ops.render.render(animation=True,scene=Scenename)"+"\n"
        + "\n" 
        "####################################"
        )

    file.close()
    
    cmd = '"' + bpy.app.binary_path + '"' + " -b " + '"' + bpy.data.filepath + '"' + " -P " + '"' + filepath + '"'

    if sys.platform.startswith("win"): 
        file = open(filepath + ".bat", 'w', encoding='utf-8')
        
        file.write("# Auto-generated by " + __addon_name__ + "\n" 
        "# " + __url__ + "\n" + "\n" 
        "# Command Line:" + "\n" + "\n" 
        "call " + cmd)
        
        file.close()
    else:  
        file = open(filepath + ".sh", 'w', encoding='utf-8')
        
        file.write(
            "# Auto-generated by " + __addon_name__ + "\n"
            "# " + __url__ + "\n" + "\n"
            "# Command Line:" + "\n" + "\n" 
            "xterm -e " + cmd)
        file.close()

        st = os.stat(filepath + ".sh")
        os.chmod(filepath + ".sh", st.st_mode | stat.S_IEXEC)

    return {'FINISHED'}
  
##################################################################

import code

namespace = {}
console = code.InteractiveConsole(locals=namespace, filename="<blender_console>")


class ImportPython(Operator, ImportHelper):
    bl_idname = "import.py"
    bl_label = "Import Render options"

    filename_ext = ".py"

    filter_glob = StringProperty(
        default="*.py",
        options={'HIDDEN'},
        maxlen=255, 
        )

    def execute(self, context):
        return open_py(self.filepath)
    
      
def open_py(filepath):

    console.push("import bpy")
    console.push("Scenename =" + '"' +bpy.context.scene.name + '"')
        
    file = open(filepath, "r") 

    for line in file: 
        line = line.strip()
        if ("bpy.data.scenes") in line:
            if (".render.") in line: 
                console.push(line)
            if (".cycles") in line:
                console.push(line)
            if (".frame") in line:
                console.push(line)
    
    return {'FINISHED'}

##################################################################  

import sys 

class RenderTerminal(bpy.types.Operator):
    
    bl_idname = "render.terminal"
    bl_label = "Render in terminal"

    def execute(self, context):
        write_py(bpy.app.tempdir + "RCL_tmp.py")
        return open_terminal()

def open_terminal():

	cmd = '"' + bpy.app.binary_path + '"' + " -b " + '"' + bpy.data.filepath + '"' + " -P " + '"' + bpy.app.tempdir + "RCL_tmp.py" + '"'
	
	if sys.platform.startswith("win"):
		file = open(bpy.app.tempdir + "RCL_tmp.bat", 'w', encoding='utf-8')

		file.write("# Auto-generated by " + __addon_name__ + "\n"
            "# " + __url__ + "\n" + "\n"
            "# Command Line:" + "\n" + "\n"
            "call " + cmd)
            
		file.close()

		os.system("start cmd /k " + bpy.app.tempdir + "RCL_tmp.bat")
	else: os.system("x-terminal-emulator -e " + cmd + "&")

	return {'FINISHED'}

##################################################################
     
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
