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
# The Original Code is Copyright (C) 2017-2018 Marcelo "Tanda" Cerviño. http://lodetanda.blogspot.com/ 
# All rights reserved.
#
# Contributor(s):
#
# ***** END GPL LICENCE BLOCK *****

bl_info = {
    "name": "RCL -Render Command Line-",
    "author": "Marcelo 'Tanda' Cerviño",
    "version": (1, 2),
    "blender": (2, 79),
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
        
        scene = context.scene
        
        blendsaved = os.path.dirname(bpy.data.filepath)
        
        split = layout.split()

        col = split.column()
        sub = col.column(align=True)
                
        sub.label(text="Import:")
        sub.operator("import.py", text="From Python")

        if blendsaved:
            col = split.column()
            sub = col.column(align=True)
            sub.label(text="Export:")
            sub.operator("export.txt", text="To Command Line")
            sub.operator("export.py", text="To Python")
             
            split = layout.split()
            sub = col.column(align=True)
            col = split.column()
            sub = col.column()
            sub.prop(scene.rcl, "options")
            layout.separator()
            split = layout.split()
            sub = col.column(align=True)
            col = split.column()
            sub = col.column()
            if scene.rcl.options:
                sub.prop(scene.rcl, "command_line")
                sub.separator()
                if not scene.rcl.command_line:
                    sub.label(text="Python Script Render Options:")
                    sub.prop(scene.rcl, "comment_line")
                    split = layout.split()
                    sub = col.column(align=True)
                    col = split.column()
                    sub = col.column()
                    
                    sub.label(text="Dimensions:")
                    sub.prop(scene.rcl, "resolution_x")
                    sub.prop(scene.rcl, "resolution_y")
                    sub.prop(scene.rcl, "resolution_percentage")
                    sub.prop(scene.rcl, "frame_start")
                    sub.prop(scene.rcl, "frame_end")
                    sub.prop(scene.rcl, "frame_step")
                    
                    sub.separator()
                    sub.label(text="Post Processing:")
                    sub.prop(scene.rcl, "dither_intensity")
                    sub.prop(scene.rcl, "use_compositing")
                    sub.prop(scene.rcl, "use_sequencer")
                    
                    sub.separator()
                    sub.label(text="Output:")
                    sub.prop(scene.rcl, "file_path")
                    sub.prop(scene.rcl, "use_placeholder")
                    sub.prop(scene.rcl, "use_overwrite")
                    sub.prop(scene.rcl, "file_extension")
                    sub.prop(scene.rcl, "use_render_cache")
                    
                    col = split.column()
                    sub = col.column(align=True)
                    
                    if bpy.data.scenes[bpy.context.scene.name].render.engine != "CYCLES": 
                        sub.label(text="Anti-Aliasing:")
                        sub.prop(scene.rcl, "use_antialiasing")
                        sub.prop(scene.rcl, "antialiasing_samples")
                        sub.prop(scene.rcl, "use_full_sample")
                    else: 
                        sub.label(text="Cycles:")
                        sub.prop(scene.rcl, "cycles_samples")
                    
                    sub.separator()
                    sub.label(text="Performance:")
                    sub.prop(scene.rcl, "threads_mode")
                    sub.prop(scene.rcl, "threads")
                    sub.prop(scene.rcl, "tile_x")
                    sub.prop(scene.rcl, "tile_y")
                    sub.prop(scene.rcl, "engine")
                    
                    sub.separator()
                    sub.label(text="Stamp:")
                    sub.prop(scene.rcl, "use_stamp")
                    
                    sub.separator()
                    sub.label(text="File Format:")
                    sub.prop(scene.rcl, "file_format")
                    if bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "BMP" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "IRIS" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "TARGA" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "TARGA_RAW" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "CINEON" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "DPX" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "HDR":
                        sub.prop(scene.rcl, "compression")
                    if bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "BMP" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "IRIS" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "JPEG" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "TARGA" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "TARGA_RAW" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "CINEON" and bpy.data.scenes[bpy.context.scene.name].render.image_settings.file_format != "HDR":
                        sub.prop(scene.rcl, "color_depth")
                    sub.prop(scene.rcl, "color_mode")
                    
                else:
                    sub.separator()
                    sub.label(text="Command Line Render Options:")
                    
                    split = layout.split()
                    sub = col.column(align=True)
                    col = split.column()
                    sub = col.column()
                    sub.label(text="Dimensions:")
                    sub.prop(scene.rcl, "frame_start")
                    sub.prop(scene.rcl, "frame_end")
                    sub.prop(scene.rcl, "frame_step")
                    
                    sub.separator()
                    sub.label(text="Output:")
                    sub.prop(scene.rcl, "file_path")
                    sub.prop(scene.rcl, "file_extension")
                    
                    col = split.column()
                    sub = col.column(align=True)
                    sub.label(text="Performance:")
                    sub.prop(scene.rcl, "threads")
                    sub.prop(scene.rcl, "engine")

                    sub.separator()
                    sub.label(text="File Format:")
                    sub.prop(scene.rcl, "file_format")
                    
                    sub.separator()
                    sub.label(text="Scene:")
                    sub.prop(scene.rcl, "scene_name")
                    
        else: layout.label(text="Blend file is not saved")
        
def render_terminal_button(self, context): 
        rd = context.scene.render
        layout = self.layout

        row = layout.row(align=True)
        row.operator("render.terminal", text="Render in Terminal", icon='CONSOLE')
    
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
        default = "*.txt",
        options = {'HIDDEN'},
        maxlen = 255, 
        )

    def execute(self, context):
        write_cl(self.filepath, context)
        self.report({'INFO'}, "Command line autorun saved in: " + self.filepath)
        return {'FINISHED'}


class ExportPython(Operator, ExportHelper):
    bl_idname = "export.py"
    bl_label = "Export Render options"

    filename_ext = ".py"

    filter_glob = StringProperty(
        default = "*.py",
        options = {'HIDDEN'},
        maxlen = 255, 
        )

    def execute(self, context):
        write_py(self.filepath, context)
        self.report({'INFO'}, "Python script and autorun saved in: " + self.filepath)
        return {'FINISHED'}

      
def write_cl(filepath, context):
    Scenename = bpy.context.scene.name
    scene = context.scene
    
    if sys.platform.startswith("win"):
        file = open(filepath + ".bat", 'w', encoding='utf-8')
    elif sys.platform.startswith("linux") :
        file = open(filepath + ".sh", 'w', encoding='utf-8')
    elif sys.platform.startswith("darwin") :
        file = open(filepath + ".sh", 'w', encoding='utf-8')

    file.write(
        "# Auto-generated by " + __addon_name__ + "\n"
        "# " + __url__ + "\n" + "\n"
        "# Command Line:" + "\n" + "\n"
    )
    if sys.platform.startswith("win"):
        file.write("call ")
    elif  sys.platform.startswith("linux") :
        file.write("xterm -e ")
    elif sys.platform.startswith("darwin") :
        file.write("open -a Terminal ")
    
    file.write(
        '"' + bpy.app.binary_path + '"' 
        + " -b " + '"' + bpy.data.filepath + '"' 
    )
    if scene.rcl.scene_name:
        file.write(
            " -S " + Scenename 
        )
    if scene.rcl.file_path:
        file.write(
            " -o " + '"' + bpy.data.scenes[Scenename].render.filepath + '"'
        )
    if scene.rcl.engine:
        file.write(
            " -E %s" % (bpy.data.scenes[Scenename].render.engine)
        )
    if scene.rcl.file_format:
        file.write(
            " -F %s" % (bpy.data.scenes[Scenename].render.image_settings.file_format) 
        )
    if scene.rcl.file_extension:
        file.write(            
            " -x %s" % (int(bpy.data.scenes[Scenename].render.use_file_extension)) 
        )
    if scene.rcl.threads:
        if bpy.data.scenes[Scenename].render.threads_mode == 'AUTO':
            file.write(" -t 0")
        else:
            file.write(
                " -t %s" % (bpy.data.scenes[Scenename].render.threads))    
    if scene.rcl.frame_start:   
        file.write(
            " -s %s" % (bpy.data.scenes[Scenename].frame_start) 
        )
    if scene.rcl.frame_end:      
        file.write(
            " -e %s" % (bpy.data.scenes[Scenename].frame_end) 
        )
    if scene.rcl.frame_step:  
        file.write(
            " -j %s" % (bpy.data.scenes[Scenename].frame_step)
        )
    file.write(
        " -a"
    )
    file.close()
        
    if sys.platform.startswith("win"):
        st = os.stat(filepath + ".bat")
        os.chmod(filepath + ".bat", st.st_mode | stat.S_IEXEC)     
    elif sys.platform.startswith("linux") :
        st = os.stat(filepath + ".sh")
        os.chmod(filepath + ".sh", st.st_mode | stat.S_IEXEC)
    elif sys.platform.startswith("darwin") :
        st = os.stat(filepath + ".sh")
        os.chmod(filepath + ".sh", st.st_mode | stat.S_IEXEC)
        
    return {'FINISHED'}


def write_py(filepath, context):
    Scenename = bpy.context.scene.name
    scene = context.scene
    
    file = open(filepath, 'w', newline='\r\n', encoding='utf-8')
    
    file.write(
        "# Auto-generated by " + __addon_name__ + "\n"
        "# " + __url__ + "\n" + "\n"
        "import bpy" + "\n" + "\n"
        "# Render Options to change" + "\n"
        "############################" + "\n" + "\n" 
        "# Scene Name" + "\n"
        "Scenename = " + '"' + Scenename + '"' + "\n" 
        + "\n"
        "# Render Quality" + "\n"
    )
    if scene.rcl.resolution_x:
        file.write(
            "bpy.data.scenes[Scenename].render.resolution_x = %s" 
            % (bpy.data.scenes[Scenename].render.resolution_x) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.resolution_x = %s" 
            % (bpy.data.scenes[Scenename].render.resolution_x) + "\n" 
        )
    if scene.rcl.resolution_y:
        file.write(
            "bpy.data.scenes[Scenename].render.resolution_y = %s" 
            % (bpy.data.scenes[Scenename].render.resolution_y) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.resolution_y = %s" 
            % (bpy.data.scenes[Scenename].render.resolution_y) + "\n" 
        )
    if scene.rcl.resolution_percentage:
        file.write(
            "bpy.data.scenes[Scenename].render.resolution_percentage = %s" 
            % (bpy.data.scenes[Scenename].render.resolution_percentage) + "\n"
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.resolution_percentage = %s" 
            % (bpy.data.scenes[Scenename].render.resolution_percentage) + "\n"
        )
        
    if bpy.data.scenes[Scenename].render.engine != "CYCLES": 
        if scene.rcl.use_antialiasing: 
            file.write(
            "bpy.data.scenes[Scenename].render.use_antialiasing = %s" 
            % (bpy.data.scenes[Scenename].render.use_antialiasing) + "\n" 
            )
        elif scene.rcl.comment_line:
            file.write(
            "#bpy.data.scenes[Scenename].render.use_antialiasing = %s" 
            % (bpy.data.scenes[Scenename].render.use_antialiasing) + "\n" 
            )
        if scene.rcl.use_antialiasing:     
            file.write(
                "bpy.data.scenes[Scenename].render.antialiasing_samples = " + '"' + "%s" 
                % (bpy.data.scenes[Scenename].render.antialiasing_samples) + '"' + "\n" 
            )
        elif scene.rcl.comment_line:
            file.write(
                "#bpy.data.scenes[Scenename].render.antialiasing_samples = " + '"' + "%s" 
                % (bpy.data.scenes[Scenename].render.antialiasing_samples) + '"' + "\n" 
            )
        if scene.rcl.use_full_sample:  
            file.write(
                "bpy.data.scenes[Scenename].render.use_full_sample = %s" 
                % (bpy.data.scenes[Scenename].render.use_full_sample) + "\n" 
            )
        elif scene.rcl.comment_line:
            file.write(
                "#bpy.data.scenes[Scenename].render.use_full_sample = %s" 
                % (bpy.data.scenes[Scenename].render.use_full_sample) + "\n" 
            )
        if scene.rcl.tile_x:  
            file.write(
                "bpy.data.scenes[Scenename].render.tile_x = %s" 
                % (bpy.data.scenes[Scenename].render.tile_x) + "\n" 
            )
        elif scene.rcl.comment_line:
            file.write(
                "#bpy.data.scenes[Scenename].render.tile_x = %s" 
                % (bpy.data.scenes[Scenename].render.tile_x) + "\n" 
            )
        if scene.rcl.tile_y:  
            file.write(    
                "bpy.data.scenes[Scenename].render.tile_y = %s" 
                % (bpy.data.scenes[Scenename].render.tile_y) + "\n" 
            )
        elif scene.rcl.comment_line:
            file.write(    
                "#bpy.data.scenes[Scenename].render.tile_y = %s" 
                % (bpy.data.scenes[Scenename].render.tile_y) + "\n" 
            )
            
    if scene.rcl.threads_mode:     
        file.write(
            "bpy.data.scenes[Scenename].render.threads_mode = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.threads_mode) + '"' + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.threads_mode = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.threads_mode) + '"' + "\n" 
        )
    if scene.rcl.threads:  
        file.write(
            "bpy.data.scenes[Scenename].render.threads = %s" 
            % (bpy.data.scenes[Scenename].render.threads) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.threads = %s" 
            % (bpy.data.scenes[Scenename].render.threads) + "\n" 
        )
    if scene.rcl.engine:  
        file.write(
            "bpy.data.scenes[Scenename].render.engine = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.engine) + '"' + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.engine = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.engine) + '"' + "\n" 
        )
        
    if bpy.data.scenes[Scenename].render.engine == "CYCLES":  
        if scene.rcl.cycles_samples:  
            file.write(
            "bpy.data.scenes[Scenename].cycles.samples = %s" 
            % (bpy.data.scenes[Scenename].cycles.samples) + "\n" 
            )
        elif scene.rcl.comment_line:
            file.write(
            "#bpy.data.scenes[Scenename].cycles.samples = %s" 
            % (bpy.data.scenes[Scenename].cycles.samples) + "\n" 
            )
    if scene.rcl.dither_intensity:      
        file.write(
            "\n"
            "bpy.data.scenes[Scenename].render.dither_intensity = %s" 
            % (bpy.data.scenes[Scenename].render.dither_intensity) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "\n"
            "#bpy.data.scenes[Scenename].render.dither_intensity = %s" 
            % (bpy.data.scenes[Scenename].render.dither_intensity) + "\n" 
        )
    if scene.rcl.use_compositing:  
        file.write(
            "bpy.data.scenes[Scenename].render.use_compositing = %s" 
            % (bpy.data.scenes[Scenename].render.use_compositing) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.use_compositing = %s" 
            % (bpy.data.scenes[Scenename].render.use_compositing) + "\n" 
        )
    if scene.rcl.use_sequencer:    
        file.write(
            "bpy.data.scenes[Scenename].render.use_sequencer = %s" 
            % (bpy.data.scenes[Scenename].render.use_sequencer) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.use_sequencer = %s" 
            % (bpy.data.scenes[Scenename].render.use_sequencer) + "\n" 
        )
        
    file.write(
        "\n"
        "# Output" + "\n"
    )
    if scene.rcl.file_path:  
        file.write(
            "bpy.data.scenes[Scenename].render.filepath = " + '"' 
            + bpy.data.scenes[Scenename].render.filepath + '"' + "\n"
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.filepath = " + '"' 
            + bpy.data.scenes[Scenename].render.filepath + '"' + "\n"
        )
    if scene.rcl.use_placeholder:  
        file.write(
            "bpy.data.scenes[Scenename].render.use_placeholder = %s" 
            % (bpy.data.scenes[Scenename].render.use_placeholder) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.use_placeholder = %s" 
            % (bpy.data.scenes[Scenename].render.use_placeholder) + "\n" 
        )
    if scene.rcl.use_overwrite:  
        file.write(
            "bpy.data.scenes[Scenename].render.use_overwrite = %s" 
            % (bpy.data.scenes[Scenename].render.use_overwrite) + "\n"
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.use_overwrite = %s" 
            % (bpy.data.scenes[Scenename].render.use_overwrite) + "\n"
        )
    if scene.rcl.file_format:   
        file.write(
            "bpy.data.scenes[Scenename].render.image_settings.file_format = " + '"' 
            + bpy.data.scenes[Scenename].render.image_settings.file_format + '"' + "\n"
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.image_settings.file_format = " + '"' 
            + bpy.data.scenes[Scenename].render.image_settings.file_format + '"' + "\n"
        )
    if bpy.data.scenes[Scenename].render.image_settings.file_format == "PNG" and scene.rcl.file_format:
        file.write( 
            "bpy.data.scenes[Scenename].render.image_settings.compression = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.compression) + "\n"
        )
        file.write(
            "bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n"
        )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "PNG" and scene.rcl.comment_line:
        file.write( 
            "#bpy.data.scenes[Scenename].render.image_settings.compression = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.compression) + "\n"
        )
        file.write(
            "#bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n"
        )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "JPEG" and scene.rcl.file_format:
        file.write(
            "bpy.data.scenes[Scenename].render.image_settings.quality = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.quality) + "\n"
            )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "JPEG" and scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.image_settings.quality = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.quality) + "\n"
            )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "TIFF" and scene.rcl.file_format:
        file.write(
            "bpy.data.scenes[Scenename].render.image_settings.tiff_codec = " + '"' 
            + (bpy.data.scenes[Scenename].render.image_settings.tiff_codec) + '"' + "\n" 
            "bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n"
            )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "TIFF" and scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.image_settings.tiff_codec = " + '"' 
            + (bpy.data.scenes[Scenename].render.image_settings.tiff_codec) + '"' + "\n" 
            "#bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n"
            )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "JPEG2000" and scene.rcl.file_format:
        file.write(
            "bpy.data.scenes[Scenename].render.image_settings.quality = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.quality) + "\n" 
        )
        file.write(
            "bpy.data.scenes[Scenename].render.image_settings.jpeg2k_codec = " + '"' 
            + (bpy.data.scenes[Scenename].render.image_settings.jpeg2k_codec) + '"' + "\n"
        )
        file.write(
            "bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_cinema_preset = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_cinema_preset) + "\n"
            "bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_cinema_48 = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_cinema_48) + "\n"
            "bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_ycc = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_ycc) + "\n" 
            "bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n"
        )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "JPEG2000" and scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.image_settings.quality = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.quality) + "\n" 
        )
        file.write(
            "#bpy.data.scenes[Scenename].render.image_settings.jpeg2k_codec = " + '"' 
            + (bpy.data.scenes[Scenename].render.image_settings.jpeg2k_codec) + '"' + "\n"
        )
        file.write(
            "#bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_cinema_preset = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_cinema_preset) + "\n"
            "#bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_cinema_48 = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_cinema_48) + "\n"
            "#bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_ycc = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_jpeg2k_ycc) + "\n" 
            "#bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n"
        )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "OPEN_EXR" and scene.rcl.file_format:
        file.write(
            "bpy.data.scenes[Scenename].render.image_settings.exr_codec = " + '"' 
            + (bpy.data.scenes[Scenename].render.image_settings.exr_codec) + '"' + "\n"
            "bpy.data.scenes[Scenename].render.image_settings.use_zbuffer = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_zbuffer) + "\n"
            "bpy.data.scenes[Scenename].render.image_settings.use_preview = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_preview) + "\n" 
            "bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n"
            )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "OPEN_EXR" and scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.image_settings.exr_codec = " + '"' 
            + (bpy.data.scenes[Scenename].render.image_settings.exr_codec) + '"' + "\n"
            "#bpy.data.scenes[Scenename].render.image_settings.use_zbuffer = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_zbuffer) + "\n"
            "#bpy.data.scenes[Scenename].render.image_settings.use_preview = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_preview) + "\n" 
            "#bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n"
            )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "OPEN_EXR_MULTILAYER" and scene.rcl.file_format:
        file.write(
            "bpy.data.scenes[Scenename].render.image_settings.exr_codec = " + '"' 
            + (bpy.data.scenes[Scenename].render.image_settings.exr_codec) + '"' + "\n"
            "bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n" 
            )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "OPEN_EXR_MULTILAYER" and scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.image_settings.exr_codec = " + '"' 
            + (bpy.data.scenes[Scenename].render.image_settings.exr_codec) + '"' + "\n"
            "#bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n" 
            )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "DPX" and scene.rcl.file_format:
        file.write(
            "bpy.data.scenes[Scenename].render.image_settings.use_cineon_log = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_cineon_log) + "\n" 
            "bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n"
            )
    elif bpy.data.scenes[Scenename].render.image_settings.file_format == "DPX" and scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.image_settings.use_cineon_log = %s" 
            % (bpy.data.scenes[Scenename].render.image_settings.use_cineon_log) + "\n" 
            "#bpy.data.scenes[Scenename].render.image_settings.color_depth = " + '"' + "%s" 
            % (bpy.data.scenes[Scenename].render.image_settings.color_depth) + '"' + "\n"
            )
    if scene.rcl.color_mode:             
        file.write(
            "bpy.data.scenes[Scenename].render.image_settings.color_mode = " + '"' 
            + bpy.data.scenes[Scenename].render.image_settings.color_mode + '"' + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.image_settings.color_mode = " + '"' 
            + bpy.data.scenes[Scenename].render.image_settings.color_mode + '"' + "\n" 
        )
    if scene.rcl.file_extension: 
        file.write(
            "bpy.data.scenes[Scenename].render.use_file_extension = %s" 
            % (bpy.data.scenes[Scenename].render.use_file_extension) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.use_file_extension = %s" 
            % (bpy.data.scenes[Scenename].render.use_file_extension) + "\n" 
        )
    if scene.rcl.use_render_cache : 
        file.write(
            "bpy.data.scenes[Scenename].render.use_render_cache = %s" 
            % (bpy.data.scenes[Scenename].render.use_render_cache) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.use_render_cache = %s" 
            % (bpy.data.scenes[Scenename].render.use_render_cache) + "\n" 
        )
        
    file.write(
        "\n" 
        "# Stamp" + "\n" 
    )
    if scene.rcl.use_stamp: 
        file.write(
            "bpy.data.scenes[Scenename].render.use_stamp = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp) + "\n" 
        )
        file.write(
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
        ) 
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].render.use_stamp = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp) + "\n" 
        )
        file.write(
            "#bpy.data.scenes[Scenename].render.stamp_font_size = %s" 
            % (bpy.data.scenes[Scenename].render.stamp_font_size) + "\n" 
            "#bpy.data.scenes[Scenename].render.stamp_background = (%.3f" 
            % (bpy.data.scenes[Scenename].render.stamp_background[0]) 
            + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_background[1])
            + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_background[2])
            + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_background[3]) + ")" + "\n" 
            "#bpy.data.scenes[Scenename].render.stamp_foreground = (%.3f" 
            % (bpy.data.scenes[Scenename].render.stamp_foreground[0])
            + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_foreground[1])
            + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_foreground[2])
            + ", %.3f" % (bpy.data.scenes[Scenename].render.stamp_foreground[3]) + ")" + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_labels = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_labels) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_time = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_render_time) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_camera = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_camera) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_date = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_date) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_lens = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_lens) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_render_time = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_render_time) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_filename = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_filename) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_frame = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_frame) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_marker = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_marker) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_scene = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_scene) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_sequencer_strip = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_sequencer_strip) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_note = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_note) + "\n" 
            "#bpy.data.scenes[Scenename].render.stamp_note_text = " + '"' 
            + bpy.data.scenes[Scenename].render.stamp_note_text + '"' + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_memory = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_memory) + "\n" 
            "#bpy.data.scenes[Scenename].render.use_stamp_strip_meta = %s" 
            % (bpy.data.scenes[Scenename].render.use_stamp_strip_meta) + "\n" 
        ) 
         
    file.write(   
        "\n"
        "# Render Frames" + "\n"
    )
    if scene.rcl.frame_start: 
        file.write(
            "bpy.data.scenes[Scenename].frame_start = %s" 
            % (bpy.data.scenes[Scenename].frame_start) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].frame_start = %s" 
            % (bpy.data.scenes[Scenename].frame_start) + "\n" 
        )
    if scene.rcl.frame_end: 
        file.write(
            "bpy.data.scenes[Scenename].frame_end = %s" 
            % (bpy.data.scenes[Scenename].frame_end) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].frame_end = %s" 
            % (bpy.data.scenes[Scenename].frame_end) + "\n" 
        )
    if scene.rcl.frame_step: 
        file.write(
            "bpy.data.scenes[Scenename].frame_step = %s" 
            % (bpy.data.scenes[Scenename].frame_step) + "\n" 
        )
    elif scene.rcl.comment_line:
        file.write(
            "#bpy.data.scenes[Scenename].frame_step = %s" 
            % (bpy.data.scenes[Scenename].frame_step) + "\n" 
        )
        
    file.write(
        "bpy.ops.render.render(animation=True,scene=Scenename)" + "\n" 
    )
    file.write(
        "\n"
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
    elif sys.platform.startswith("linux"):
        file = open(filepath + ".sh", 'w', encoding='utf-8')
        
        file.write(
            "# Auto-generated by " + __addon_name__ + "\n"
            "# " + __url__ + "\n" + "\n"
            "# Command Line:" + "\n" + "\n" 
            "xterm -e " + cmd)
        file.close()

        st = os.stat(filepath + ".sh")
        os.chmod(filepath + ".sh", st.st_mode | stat.S_IEXEC)
    elif sys.platform.startswith("darwin"):
        file = open(filepath + ".sh", 'w', encoding='utf-8')
        
        file.write(
            "# Auto-generated by " + __addon_name__ + "\n"
            "# " + __url__ + "\n" + "\n"
            "# Command Line:" + "\n" + "\n" 
            "open -a Terminal " + cmd)
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
        default = "*.py",
        options = {'HIDDEN'},
        maxlen = 255, 
        )

    def execute(self, context):
        open_py(self.filepath)
        self.report({'INFO'}, "Render options imported from: " + self.filepath)
        return {'FINISHED'}
    
    
def open_py(filepath):
    console.push("import bpy")
    console.push("Scenename =" + '"' +bpy.context.scene.name + '"')
        
    file = open(filepath, "r") 

    for line in file: 
        line = line.strip()
        if "bpy.data.scenes" in line:
            if ".render." in line: 
                print("Render options imported: ")
                console.push(line)
                print(line)
            if ".cycles" in line:
                print("Cycles options imported: ")
                console.push(line)
                print(line)
            if ".frame" in line:
                print("Frame options imported: ")
                console.push(line)
                print(line)
                   
    return {'FINISHED'}

##################################################################  

import sys 

class RenderTerminal(bpy.types.Operator):
    bl_idname = "render.terminal"
    bl_label = "Render in terminal"

    def execute(self, context):
        blendsaved = os.path.dirname(bpy.data.filepath)
        if blendsaved:
            write_py(bpy.app.tempdir + "RCL_tmp.py", context)
            open_terminal()
            self.report({'INFO'}, "Rendering in background you can close Blender")
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Blend file is not saved")
            return {'FINISHED'}
        
        
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
        
    elif sys.platform.startswith("linux"): os.system("x-terminal-emulator -e " + cmd + "&")
    elif sys.platform.startswith("darwin"): os.system("open -a Terminal " + cmd + "&")
            
    return {'FINISHED'}

from bpy.props import BoolProperty, PointerProperty
from bpy.types import PropertyGroup, Panel

class rclProperty(PropertyGroup):
    options = BoolProperty(
        name = "Available Options",
        default = False
    )
    
    command_line = BoolProperty(
        name = "For Command Line",
        default = False
    )
    
    comment_line = BoolProperty(
        name = "Add Python comment line '#'",
        default = True
    )
    
    resolution_x = BoolProperty(
        name = "Resolution X",
        default = True
    )
    resolution_y = BoolProperty(
        name = "Resolution Y",
        default = True
    )
    resolution_percentage = BoolProperty(
        name = "Percentage",
        default = True
    )
    frame_start = BoolProperty(
        name="Start Frame",
        default = True
    )
    frame_end = BoolProperty(
        name = "End Frame",
        default = True
    )
    frame_step = BoolProperty(
        name="Frame Step",
        default = False
    )
    
    use_antialiasing = BoolProperty(
        name = "Anti-Aliasing",
        default = False
    )
    antialiasing_samples = BoolProperty(
        name = "Samples",
        default = False
    )
    use_full_sample = BoolProperty(
        name = "Full Sample",
        default = False
    )
    
    threads_mode = BoolProperty(
        name = "Threads Mode",
        default = False
    )
    threads = BoolProperty(
        name = "Threads",
        default = True
    )
    tile_x = BoolProperty(
        name = "Tile X",
        default = False
    )
    tile_y = BoolProperty(
        name = "Tile Y",
        default = False
    )
    engine = BoolProperty(
        name = "Render Engine",
        default = False
    )
    
    cycles_samples = BoolProperty(
        name = "Render Samples",
        default = True
    )
    
    dither_intensity = BoolProperty(
        name = "Dither",
        default = False
    )
    use_compositing = BoolProperty(
        name = "Compositing",
        default = False
    )
    use_sequencer = BoolProperty(
        name = "Sequencer",
        default = False
    )
    
    file_path = BoolProperty(
        name = "Output Path",
        default = True
    )
    use_placeholder = BoolProperty(
        name = "Placeholder",
        default = False
    )
    use_overwrite = BoolProperty(
        name = "Overwrite",
        default = False
    )
    file_extension = BoolProperty(
        name = "File Extension",
        default = True
    )
    use_render_cache = BoolProperty(
        name = "Cache Result",
        default = False
    )
    
    file_format = BoolProperty(
        name = "File Format",
        default = True
    )
    compression = BoolProperty(
        name = "Compression",
        default = False
    )
    color_depth = BoolProperty(
        name = "Color Depth",
        default = False
    )
    color_mode = BoolProperty(
        name = "Color Mode",
        default = False
    )
    
    use_stamp = BoolProperty(
        name = "Stamp",
        default = False
    )
    
    scene_name = BoolProperty(
        name = "Scene Name",
        default = True
    )
    
##################################################################
     
def register():
    bpy.utils.register_module(__name__)
    bpy.types.RENDER_PT_render.append(render_terminal_button)
    bpy.types.Scene.rcl = PointerProperty(type=rclProperty)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.RENDER_PT_render.remove(render_terminal_button)
    del(bpy.types.Scene.rcl)

if __name__ == "__main__":
    register()
