/**
 * Waves Pins Three.js — Hero background (sans GUI).
 * Adapté pour LPPP-OppyAI, couleurs charte Oppy (cyan/turquoise).
 * Position fixe viewport, parallaxe.
 */
(function() {
    function init() {
        if (typeof THREE === 'undefined') return;
        var container = document.getElementById('hero-waves-pins-container');
        if (!container) return;

        var params = {
            gap: 1.3224,
            speed: 0.034,
            waveHeight: 6.4,
            frequencyX: 0.42,
            frequencyZ: 0.78,
            chaosScale: 9.2,
            randomWobble: 2.85,
            randomSpeed: 1.65,
            dotSize: 0.45441,
            dotOpacity: 0.769,
            lineLength: 9.804,
            lineOpacity: 0.449,
            lineGrowth: true,
            colorStart: '#8612b7',
            colorEnd: '#06777c',
            fogColor: '#070023',
            fogDensity: 0.0185,
            camX: -3.7, camY: 10.5, camZ: 15.147
        };

        var ROWS = 50, COLS = 100;
        var scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(params.fogColor, params.fogDensity);
        scene.background = new THREE.Color(params.fogColor);

        var camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
        var renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        container.appendChild(renderer.domElement);

        function createCircleTexture() {
            var canvas = document.createElement('canvas');
            canvas.width = 32; canvas.height = 32;
            var ctx = canvas.getContext('2d');
            var grad = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
            grad.addColorStop(0, 'rgba(255,255,255,1)');
            grad.addColorStop(1, 'rgba(255,255,255,0)');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 32, 32);
            return new THREE.CanvasTexture(canvas);
        }

        var particleCount = ROWS * COLS;
        var particlesGeometry = new THREE.BufferGeometry();
        var particlePositions = new Float32Array(particleCount * 3);
        var particleColors = new Float32Array(particleCount * 3);
        var linesGeometry = new THREE.BufferGeometry();
        var linePositions = new Float32Array(particleCount * 2 * 3);
        var lineColors = new Float32Array(particleCount * 2 * 3);

        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));
        particlesGeometry.setAttribute('color', new THREE.BufferAttribute(particleColors, 3));
        linesGeometry.setAttribute('position', new THREE.BufferAttribute(linePositions, 3));
        linesGeometry.setAttribute('color', new THREE.BufferAttribute(lineColors, 3));

        function updateLayout() {
            var offsetX = (COLS * params.gap) / 2;
            var offsetZ = (ROWS * params.gap) / 2;
            var i = 0, lineIndex = 0;
            for (var x = 0; x < COLS; x++) {
                for (var z = 0; z < ROWS; z++) {
                    var px = x * params.gap - offsetX;
                    var pz = z * params.gap - offsetZ;
                    particlePositions[i * 3] = px;
                    particlePositions[i * 3 + 2] = pz;
                    linePositions[lineIndex * 3] = px;
                    linePositions[lineIndex * 3 + 2] = pz;
                    linePositions[(lineIndex + 1) * 3] = px;
                    linePositions[(lineIndex + 1) * 3 + 2] = pz;
                    i++;
                    lineIndex += 2;
                }
            }
            particlesGeometry.attributes.position.needsUpdate = true;
            linesGeometry.attributes.position.needsUpdate = true;
        }

        function updateColors() {
            var c1 = new THREE.Color(params.colorStart);
            var c2 = new THREE.Color(params.colorEnd);
            var pColors = particlesGeometry.attributes.color.array;
            var lColors = linesGeometry.attributes.color.array;
            var j = 0, l = 0;
            for (var x = 0; x < COLS; x++) {
                var mixRatio = x / COLS;
                var mixedColor = c1.clone().lerp(c2, mixRatio);
                for (var z = 0; z < ROWS; z++) {
                    pColors[j * 3] = mixedColor.r;
                    pColors[j * 3 + 1] = mixedColor.g;
                    pColors[j * 3 + 2] = mixedColor.b;
                    lColors[l * 3] = mixedColor.r;
                    lColors[l * 3 + 1] = mixedColor.g;
                    lColors[l * 3 + 2] = mixedColor.b;
                    lColors[(l + 1) * 3] = mixedColor.r * 0.3;
                    lColors[(l + 1) * 3 + 1] = mixedColor.g * 0.3;
                    lColors[(l + 1) * 3 + 2] = mixedColor.b * 0.3;
                    j++;
                    l += 2;
                }
            }
            particlesGeometry.attributes.color.needsUpdate = true;
            linesGeometry.attributes.color.needsUpdate = true;
        }

        updateLayout();
        updateColors();

        var particlesMaterial = new THREE.PointsMaterial({
            size: params.dotSize,
            map: createCircleTexture(),
            vertexColors: true,
            transparent: true,
            opacity: params.dotOpacity,
            blending: THREE.AdditiveBlending,
            depthWrite: false
        });
        var linesMaterial = new THREE.LineBasicMaterial({
            vertexColors: true,
            transparent: true,
            opacity: params.lineOpacity,
            blending: THREE.AdditiveBlending
        });

        var particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
        var linesMesh = new THREE.LineSegments(linesGeometry, linesMaterial);
        scene.add(particlesMesh);
        scene.add(linesMesh);

        camera.position.set(params.camX, params.camY, params.camZ);
        camera.lookAt(0, 0, 0);

        var time = 0;
        var floorLevel = -5.0;

        function resize() {
            var rect = container.getBoundingClientRect();
            var w = rect.width || window.innerWidth;
            var h = rect.height || window.innerHeight;
            if (w <= 0 || h <= 0) {
                w = window.innerWidth;
                h = window.innerHeight;
            }
            renderer.setSize(w, h);
            camera.aspect = w / h;
            camera.updateProjectionMatrix();
        }

        function animate() {
            requestAnimationFrame(animate);
            var t = time;
            var tFast = t * params.randomSpeed;
            time += params.speed * (0.88 + 0.24 * Math.sin(performance.now() * 0.0004));

            var pPos = particlesGeometry.attributes.position.array;
            var lPos = linesGeometry.attributes.position.array;
            var i = 0, lineIdx = 0;

            for (var x = 0; x < COLS; x++) {
                for (var z = 0; z < ROWS; z++) {
                    var px = pPos[i * 3];
                    var pz = pPos[i * 3 + 2];
                    var phase = (x * 17 + z * 31 + i * 13) * 0.019;
                    var py = Math.sin(px * params.frequencyX + t) * params.waveHeight +
                             Math.cos(pz * params.frequencyZ + t * 0.62) * params.waveHeight +
                             Math.sin((px + pz) * 0.12 + t * 1.15) * params.chaosScale +
                             Math.sin(px * 0.37 + tFast + phase) * params.randomWobble +
                             Math.cos(pz * 0.29 + tFast * 1.08 + phase * 1.7) * params.randomWobble * 0.85 +
                             Math.sin((px * pz) * 0.018 + t * 2.4 + i * 0.07) * params.chaosScale * 0.35;

                    pPos[i * 3 + 1] = py;

                    if (params.lineGrowth) {
                        lPos[lineIdx * 3 + 1] = py;
                        lPos[(lineIdx + 1) * 3 + 1] = floorLevel;
                    } else {
                        lPos[lineIdx * 3 + 1] = py;
                        lPos[(lineIdx + 1) * 3 + 1] = py - params.lineLength;
                    }
                    i++;
                    lineIdx += 2;
                }
            }

            particlesGeometry.attributes.position.needsUpdate = true;
            linesGeometry.attributes.position.needsUpdate = true;
            renderer.render(scene, camera);
        }

        window.addEventListener('resize', resize);
        resize();
        animate();
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
