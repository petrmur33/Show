#ifdef GL_ES
precision highp float;
#endif

// glslsandbox uniforms
uniform float time;
uniform vec2 resolution;
uniform vec2 mouse;

// shadertoy emulation
uniform sampler2D iChannel1;
uniform sampler2D iChannel2;
uniform sampler2D iChannel0;
#define iTime time
#define iResolution resolution

#define t iTime
#define r iResolution.xy
#define iMouse mouse

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    vec2 uv = fragCoord / iResolution.xy;
    
    vec4 color = texture(iChannel0, uv);
    
    fragColor = vec4(color.xyz, 1);
}

void main() {
    mainImage(gl_FragColor, gl_FragCoord.xy);
}
