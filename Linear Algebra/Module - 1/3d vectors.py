import numpy as np
from manim import *


class VectorDimensions(ThreeDScene):
    def construct(self):
        
        self.camera.background_color = BLACK

        
        
        stars = VGroup()
        for _ in range(50):
            x = np.random.uniform(-7, 7)
            y = np.random.uniform(-5, 5)
            z = np.random.uniform(-5, 5)
            stars.add(Dot(point=[x, y, z], radius=0.03, color=GREY_E))
        self.add_fixed_in_frame_mobjects(stars)  
        
        self.remove(stars)  
        self.add(stars)  

        
        COL_X = RED
        COL_Y = GREEN
        COL_Z = BLUE
        COL_VEC = YELLOW
        COL_BASIS = ORANGE

        
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        

        vector_2d_vals = [[3], [2]]
        matrix_2d = Matrix(vector_2d_vals, include_background_rectangle=True)
        matrix_2d.get_brackets().set_color(WHITE)
        ent = matrix_2d.get_entries()
        ent[0].set_color(COL_X)
        ent[1].set_color(COL_Y)
        matrix_2d.scale(1.5)

        x_label = MathTex("x", color=COL_X).next_to(matrix_2d.get_rows()[0], RIGHT)
        y_label = MathTex("y", color=COL_Y).next_to(matrix_2d.get_rows()[1], RIGHT)

        self.play(FadeIn(matrix_2d, scale=0.5))
        self.play(FadeIn(x_label, shift=LEFT), FadeIn(y_label, shift=LEFT))
        self.wait(0.5)

        self.play(FadeOut(x_label), FadeOut(y_label))
        self.play(matrix_2d.animate.to_corner(UL).scale(0.7))

        

        plane = NumberPlane(
            x_range=[-2, 6, 1],
            y_range=[-2, 6, 1],
            background_line_style={
                "stroke_color": GREY_D,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            },
            axis_config={"stroke_color": GREY_B, "include_tip": True}
        )
        plane.add_coordinates()

        x_axis_lab = plane.get_x_axis_label("x").set_color(COL_X)
        y_axis_lab = plane.get_y_axis_label("y").set_color(COL_Y)

        self.play(
            Create(plane, run_time=2, lag_ratio=0.1),
            FadeIn(x_axis_lab),
            FadeIn(y_axis_lab)
        )

        
        
        p0 = plane.coords_to_point(0, 0, 0)
        p1 = plane.coords_to_point(3, 0, 0)
        p2 = plane.coords_to_point(3, 2, 0)

        
        
        eq_text = MathTex("\\vec{v} =", "3\\hat{i}", "+", "2\\hat{j}", color=WHITE).to_corner(UR)
        eq_text[1].set_color(COL_X)
        eq_text[3].set_color(COL_Y)
        self.play(Write(eq_text[0]))  

        
        trace_dot_x = Dot(p0, color=COL_X)
        trace_line_x = Line(p0, p1, color=COL_X, stroke_width=4)

        self.add(trace_dot_x)
        self.play(
            trace_dot_x.animate.move_to(p1),
            Create(trace_line_x),
            FadeIn(eq_text[1], shift=LEFT),  
            run_time=1.5
        )

        
        
        elbow_len = 0.4
        elbow_1 = Line(plane.coords_to_point(3 - elbow_len, 0, 0), plane.coords_to_point(3 - elbow_len, elbow_len, 0),
                       color=GREY_A)
        elbow_2 = Line(plane.coords_to_point(3 - elbow_len, elbow_len, 0), plane.coords_to_point(3, elbow_len, 0),
                       color=GREY_A)
        corner_xy = VGroup(elbow_1, elbow_2)

        
        trace_dot_y = Dot(p1, color=COL_Y)
        trace_line_y = Line(p1, p2, color=COL_Y, stroke_width=4)

        self.remove(trace_dot_x)
        self.add(trace_dot_y)

        self.play(
            trace_dot_y.animate.move_to(p2),
            Create(trace_line_y),
            FadeIn(eq_text[2]),  
            FadeIn(eq_text[3], shift=LEFT),  
            Create(corner_xy),
            run_time=1.5
        )
        self.remove(trace_dot_y)

        
        vector = Arrow(p0, p2, buff=0, color=COL_VEC, max_stroke_width_to_length_ratio=5)
        vector_label = MathTex("\\vec{v}", color=COL_VEC).next_to(p2, UP + RIGHT, buff=0.1)

        self.play(GrowArrow(vector), Write(vector_label))

        
        self.play(Flash(p2, color=COL_VEC, line_length=0.3, num_lines=12))
        self.wait(1)

        

        
        self.play(
            FadeOut(plane),
            FadeOut(vector),
            FadeOut(vector_label),
            FadeOut(trace_line_x),
            FadeOut(trace_line_y),
            FadeOut(corner_xy),
            FadeOut(x_axis_lab),
            FadeOut(y_axis_lab),
            FadeOut(eq_text)
        )

        
        vector_3d_vals = [[3], [2], [5]]
        matrix_3d = Matrix(vector_3d_vals, include_background_rectangle=True).scale(1.5 * 0.7).to_corner(UL)
        ent_3d = matrix_3d.get_entries()
        ent_3d[0].set_color(COL_X)
        ent_3d[1].set_color(COL_Y)
        ent_3d[2].set_color(COL_Z)

        z_label_mat = MathTex("z", color=COL_Z).next_to(matrix_3d.get_rows()[2], RIGHT)

        self.play(Transform(matrix_2d, matrix_3d))
        self.play(Indicate(z_label_mat))
        self.wait(0.5)
        self.play(FadeOut(z_label_mat))

        

        axes = ThreeDAxes(
            x_range=[-2, 6, 1],
            y_range=[-2, 6, 1],
            z_range=[-2, 6, 1],
            axis_config={"include_tip": True}
        )
        axes.x_axis.set_color(COL_X)
        axes.y_axis.set_color(COL_Y)
        axes.z_axis.set_color(COL_Z)

        
        
        self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES, zoom=0.7, run_time=3, added_anims=[
            Create(axes),
        ])

        
        shockwave = Circle(radius=0.1, color=COL_Z, stroke_width=8).rotate(90 * DEGREES, RIGHT)
        self.play(
            shockwave.animate.scale(30).set_stroke(width=0, opacity=0),
            run_time=1.5
        )

        
        
        basis_i = Arrow(axes.c2p(0, 0, 0), axes.c2p(1, 0, 0), color=COL_BASIS, buff=0)
        basis_j = Arrow(axes.c2p(0, 0, 0), axes.c2p(0, 1, 0), color=COL_BASIS, buff=0)
        basis_k = Arrow(axes.c2p(0, 0, 0), axes.c2p(0, 0, 1), color=COL_BASIS, buff=0)

        self.play(Create(basis_i), Create(basis_j), Create(basis_k), run_time=0.5)
        self.play(FadeOut(basis_i), FadeOut(basis_j), FadeOut(basis_k), run_time=0.5)

        
        origin = axes.c2p(0, 0, 0)
        point_xy = axes.c2p(3, 2, 0)
        point_xyz = axes.c2p(3, 2, 5)

        
        shadow_vector = Arrow(origin, point_xy, buff=0, color=GREY, stroke_opacity=0.5)

        
        proj_x = DashedLine(axes.c2p(3, 0, 0), point_xy, color=COL_Y)
        proj_y = DashedLine(axes.c2p(0, 2, 0), point_xy, color=COL_X)
        proj_z = DashedLine(point_xy, point_xyz, color=COL_Z)

        self.play(Create(shadow_vector), run_time=1)
        self.play(Create(proj_x), Create(proj_y))

        
        self.play(Create(proj_z))

        
        vector_3d = Arrow3D(
            start=origin,
            end=point_xyz,
            color=COL_VEC
        )

        self.play(Create(vector_3d), run_time=1.5)

        
        
        flash_sphere = Sphere(center=point_xyz, radius=0.1, color=COL_VEC).set_opacity(0.8)
        self.play(
            FadeIn(flash_sphere, scale=0.1),
            run_time=0.3
        )
        self.play(
            flash_sphere.animate.scale(2).set_opacity(0),
            run_time=0.5
        )
        self.remove(flash_sphere)

        
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        

        
        self.play(
            FadeOut(axes),
            FadeOut(vector_3d),
            FadeOut(shadow_vector),
            FadeOut(proj_x),
            FadeOut(proj_y),
            FadeOut(proj_z),
            FadeOut(stars),  
            run_time=1.0
        )

        self.move_camera(phi=0, theta=-90, zoom=1, run_time=1.5)

        
        
        n_dim_matrix = Matrix([["x_1"], ["x_2"], ["\\vdots"], ["x_n"]], v_buff=0.6)
        n_dim_matrix.set_color(WHITE).scale(1.2)

        
        tunnel = VGroup()
        for i in range(1, 6):
            copy_m = n_dim_matrix.copy()
            copy_m.scale(1 - i * 0.15)  
            copy_m.set_opacity(0.8 - i * 0.15)  
            copy_m.move_to(RIGHT * i * 0.5 + UP * i * 0.3)  
            
            
            
            copy_m.move_to(ORIGIN)
            tunnel.add(copy_m)

        tunnel.arrange(IN, buff=0.5)  

        
        tunnel = VGroup()
        for i in range(8):
            m = n_dim_matrix.copy()
            scale_factor = 0.6 ** i
            m.scale(scale_factor)
            m.set_opacity(0.8 ** i)
            tunnel.add(m)

        
        self.play(
            ReplacementTransform(matrix_2d, tunnel[0]),
            Create(tunnel[1:]),  
            run_time=2
        )

        title = Text("N-Dimensions", font_size=40, weight=BOLD).to_edge(UP)
        subtitle = Text("Mathematically consistent.\nVisually impossible.", font_size=24, color=GREY).next_to(tunnel[0],
                                                                                                              DOWN,
                                                                                                              buff=1)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))

        
        self.play(
            tunnel.animate.scale(1.1).set_color(COL_VEC),
            rate_func=there_and_back,
            run_time=2
        )

        self.wait(2)
