// JavaScript logic for Bunkový Vesmír interactive portal

document.addEventListener('DOMContentLoaded', () => {
    // 1. Tab switching logic
    const navBtn = document.querySelectorAll('.nav-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    navBtn.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active classes
            navBtn.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(t => t.classList.remove('active'));

            // Add active classes to current tab
            btn.classList.add('active');
            const tabId = btn.getAttribute('data-tab');
            document.getElementById(tabId).classList.add('active');

            // Trigger canvas resizing if needed
            if (tabId === 'tab-simulations') {
                initBfsSim();
                initDowrySim();
            }
        });
    });

    // 2. Interactive Calculator Logic
    const inputK = document.getElementById('input-k');
    const inputC = document.getElementById('input-c');
    const displayK = document.getElementById('display-k');
    const displayC = document.getElementById('display-c');

    const calcDelta = document.getElementById('calc-delta');
    const calcEpsilon = document.getElementById('calc-epsilon');
    const calcNs1 = document.getElementById('calc-ns1');
    const calcNs2 = document.getElementById('calc-ns2');

    function updateCalculator() {
        const k = parseFloat(inputK.value);
        const c = parseInt(inputC.value, 10);

        displayK.textContent = k.toFixed(3);
        displayC.textContent = c;

        // Formula: delta = 1 / (k + C)
        const delta = 1 / (k + c);
        // Formula: epsilon = 1.5 * delta
        const epsilon = 1.5 * delta;
        
        // 1st order: ns - 1 = -epsilon  => ns = 1 - epsilon
        const ns1 = 1 - epsilon;
        // 2nd order: ns - 1 = -epsilon / (1 - epsilon) => ns = 1 - epsilon / (1 - epsilon)
        const ns2 = 1 - (epsilon / (1 - epsilon));

        calcDelta.textContent = delta.toFixed(5);
        calcEpsilon.textContent = epsilon.toFixed(5);
        calcNs1.textContent = ns1.toFixed(4);
        calcNs2.textContent = ns2.toFixed(4);
    }

    inputK.addEventListener('input', updateCalculator);
    inputC.addEventListener('input', updateCalculator);
    updateCalculator(); // Run once initially

    // 3. Canvas Simulation 1: BFS Causal Network Propagation (KPZ & Light Cone)
    let bfsCanvas = document.getElementById('canvas-bfs');
    let bfsCtx = bfsCanvas.getContext('2d');
    let nodes = [];
    let bfsQueue = [];
    let bfsVisited = new Set();
    let bfsT = 0;
    let bfsTimer = null;
    let startNodeIndex = 0;

    function initBfsSim() {
        if (bfsTimer) clearInterval(bfsTimer);
        bfsT = 0;
        document.getElementById('stats-bfs-t').textContent = bfsT;
        bfsVisited.clear();
        bfsQueue = [];

        nodes = [];
        const nodeCount = 120;
        const width = bfsCanvas.width;
        const height = bfsCanvas.height;

        // Generate random nodes
        for (let i = 0; i < nodeCount; i++) {
            nodes.push({
                x: 30 + Math.random() * (width - 60),
                y: 30 + Math.random() * (height - 60),
                visited: false,
                level: -1,
                neighbors: []
            });
        }

        // Connect nodes based on distance (Poisson/Delaunay-like approximation)
        const maxDist = 65;
        for (let i = 0; i < nodeCount; i++) {
            for (let j = i + 1; j < nodeCount; j++) {
                const dist = Math.hypot(nodes[i].x - nodes[j].x, nodes[i].y - nodes[j].y);
                if (dist < maxDist) {
                    nodes[i].neighbors.push(j);
                    nodes[j].neighbors.push(i);
                }
            }
        }

        // Find the node closest to center as start
        let minDistToCenter = Infinity;
        for (let i = 0; i < nodeCount; i++) {
            const dist = Math.hypot(nodes[i].x - width/2, nodes[i].y - height/2);
            if (dist < minDistToCenter) {
                minDistToCenter = dist;
                startNodeIndex = i;
            }
        }

        drawBfs();
    }

    function drawBfs() {
        bfsCtx.fillStyle = '#050508';
        bfsCtx.fillRect(0, 0, bfsCanvas.width, bfsCanvas.height);

        // Draw connections
        bfsCtx.strokeStyle = 'rgba(100, 100, 150, 0.12)';
        bfsCtx.lineWidth = 1.2;
        for (let i = 0; i < nodes.length; i++) {
            nodes[i].neighbors.forEach(nIndex => {
                if (nIndex > i) {
                    bfsCtx.beginPath();
                    bfsCtx.moveTo(nodes[i].x, nodes[i].y);
                    bfsCtx.lineTo(nodes[nIndex].x, nodes[nIndex].y);
                    bfsCtx.stroke();
                }
            });
        }

        // Draw nodes
        nodes.forEach((node, i) => {
            bfsCtx.beginPath();
            bfsCtx.arc(node.x, node.y, 4, 0, Math.PI * 2);
            if (node.visited) {
                // Front nodes
                if (node.level === bfsT) {
                    bfsCtx.fillStyle = '#06b6d4'; // Glowing Cyan
                    bfsCtx.shadowColor = '#06b6d4';
                    bfsCtx.shadowBlur = 8;
                } else {
                    bfsCtx.fillStyle = '#8b5cf6'; // Visited Violet
                    bfsCtx.shadowBlur = 0;
                }
            } else {
                bfsCtx.fillStyle = '#2d3748'; // Gray unvisited
                bfsCtx.shadowBlur = 0;
            }
            bfsCtx.fill();
        });
        bfsCtx.shadowBlur = 0; // reset
    }

    function stepBfs() {
        if (bfsQueue.length === 0) {
            clearInterval(bfsTimer);
            return;
        }

        bfsT++;
        document.getElementById('stats-bfs-t').textContent = bfsT;
        let nextQueue = [];

        bfsQueue.forEach(nIndex => {
            nodes[nIndex].neighbors.forEach(neighborIndex => {
                if (!bfsVisited.has(neighborIndex)) {
                    bfsVisited.add(neighborIndex);
                    nodes[neighborIndex].visited = true;
                    nodes[neighborIndex].level = bfsT;
                    nextQueue.push(neighborIndex);
                }
            });
        });

        bfsQueue = nextQueue;
        drawBfs();

        if (bfsQueue.length === 0) {
            clearInterval(bfsTimer);
        }
    }

    document.getElementById('btn-start-bfs').addEventListener('click', () => {
        initBfsSim();
        // Set root node
        nodes[startNodeIndex].visited = true;
        nodes[startNodeIndex].level = 0;
        bfsVisited.add(startNodeIndex);
        bfsQueue.push(startNodeIndex);
        
        drawBfs();

        if (bfsTimer) clearInterval(bfsTimer);
        bfsTimer = setInterval(stepBfs, 300);
    });

    document.getElementById('btn-reset-bfs').addEventListener('click', initBfsSim);

    // 4. Canvas Simulation 2: Dowry Rule Convergence Plotter (Atractor C=28)
    let dowryCanvas = document.getElementById('canvas-dowry');
    let dowryCtx = dowryCanvas.getContext('2d');
    let dowryHistory = [];
    let dowryGen = 0;
    let currentN = 2.0; // Starts at 2 (skromné veno)
    let dowryTimer = null;

    function initDowrySim() {
        if (dowryTimer) clearInterval(dowryTimer);
        dowryGen = 0;
        currentN = 2.0;
        dowryHistory = [currentN];
        document.getElementById('stats-dowry-g').textContent = dowryGen;
        document.getElementById('stats-dowry-nv').textContent = currentN.toFixed(2);
        drawDowry();
    }

    function drawDowry() {
        dowryCtx.fillStyle = '#050508';
        dowryCtx.fillRect(0, 0, dowryCanvas.width, dowryCanvas.height);

        const width = dowryCanvas.width;
        const height = dowryCanvas.height;

        // Draw grids
        dowryCtx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
        dowryCtx.lineWidth = 1;
        for (let i = 0; i <= 10; i++) {
            const x = 50 + (i / 10) * (width - 70);
            const y = 30 + (i / 10) * (height - 60);

            // vertical grid
            dowryCtx.beginPath();
            dowryCtx.moveTo(x, 30);
            dowryCtx.lineTo(x, height - 30);
            dowryCtx.stroke();

            // horizontal grid
            dowryCtx.beginPath();
            dowryCtx.moveTo(50, y);
            dowryCtx.lineTo(width - 20, y);
            dowryCtx.stroke();
        }

        // Draw attractor line (C = 28)
        const cVal = 28;
        const targetY = height - 30 - (cVal / 35) * (height - 60);
        dowryCtx.strokeStyle = 'rgba(16, 185, 129, 0.4)';
        dowryCtx.lineWidth = 1.5;
        dowryCtx.setLineDash([5, 5]);
        dowryCtx.beginPath();
        dowryCtx.moveTo(50, targetY);
        dowryCtx.lineTo(width - 20, targetY);
        dowryCtx.stroke();
        dowryCtx.setLineDash([]); // Reset line dash

        dowryCtx.fillStyle = '#10b981';
        dowryCtx.font = '10px Inter';
        dowryCtx.fillText('Atraktor C = 28', width - 110, targetY - 5);

        // Draw Axes
        dowryCtx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        dowryCtx.lineWidth = 1.5;
        dowryCtx.beginPath();
        dowryCtx.moveTo(50, 30);
        dowryCtx.lineTo(50, height - 30);
        dowryCtx.lineTo(width - 20, height - 30);
        dowryCtx.stroke();

        // Draw labels
        dowryCtx.fillStyle = '#9ca3af';
        dowryCtx.fillText('Generácie', width - 75, height - 12);
        dowryCtx.save();
        dowryCtx.translate(18, height / 2 + 10);
        dowryCtx.rotate(-Math.PI / 2);
        dowryCtx.fillText('Počet V-spojení', 0, 0);
        dowryCtx.restore();

        // Draw history curve
        if (dowryHistory.length > 1) {
            dowryCtx.strokeStyle = '#8b5cf6'; // Violet line
            dowryCtx.lineWidth = 2.5;
            dowryCtx.beginPath();

            const xStep = (width - 70) / Math.max(10, dowryHistory.length - 1);
            dowryHistory.forEach((val, idx) => {
                const x = 50 + idx * xStep;
                const y = height - 30 - (val / 35) * (height - 60);
                if (idx === 0) {
                    dowryCtx.moveTo(x, y);
                } else {
                    dowryCtx.lineTo(x, y);
                }
            });
            dowryCtx.stroke();

            // Draw points
            dowryCtx.fillStyle = '#06b6d4';
            dowryHistory.forEach((val, idx) => {
                const x = 50 + idx * xStep;
                const y = height - 30 - (val / 35) * (height - 60);
                dowryCtx.beginPath();
                dowryCtx.arc(x, y, 4, 0, Math.PI*2);
                dowryCtx.fill();
            });
        }
    }

    function stepDowry() {
        dowryGen++;
        // Formula: n_next = n / 2 + C / 2
        currentN = currentN / 2 + 28 / 2;
        dowryHistory.push(currentN);
        document.getElementById('stats-dowry-g').textContent = dowryGen;
        document.getElementById('stats-dowry-nv').textContent = currentN.toFixed(2);
        drawDowry();
    }

    document.getElementById('btn-step-dowry').addEventListener('click', stepDowry);

    document.getElementById('btn-auto-dowry').addEventListener('click', () => {
        initDowrySim();
        if (dowryTimer) clearInterval(dowryTimer);
        dowryTimer = setInterval(() => {
            if (dowryGen < 15) {
                stepDowry();
            } else {
                clearInterval(dowryTimer);
            }
        }, 400);
    });

    // Initialize simulations once
    initBfsSim();
    initDowrySim();
});
