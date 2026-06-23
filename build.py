#!/usr/bin/env python3
"""Write the improved index.html for the project."""
import os

OUT = "/home/user/project/docs/index.html"

# Read the CSS from a separate approach - write it directly
html_content = r"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Авторизация</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="theme-color" content="#1a1a2e">
    <style>
        :root {
            --bg: #f0f2f5;
            --surface: #ffffff;
            --surface-alt: #f8f9fb;
            --text: #1a1a2e;
            --text-secondary: #5a5d6e;
            --text-muted: #8b8fa3;
            --border: #e2e5ec;
            --border-light: #eef0f4;
            --primary: #4f6ef7;
            --primary-hover: #3d5bd9;
            --primary-light: #eef1fe;
            --primary-glow: rgba(79,110,247,0.15);
            --success: #22c55e;
            --success-light: #eafaf1;
            --warning: #f59e0b;
            --warning-light: #fffbe6;
            --warning-border: #fbbf24;
            --danger: #ef4444;
            --danger-light: #fef2f2;
            --android: #689f38;
            --android-light: #edf7e7;
            --android-glow: rgba(104,159,56,0.15);
            --console: #6d28d9;
            --console-light: #f3eeff;
            --radius-sm: 8px;
            --radius: 12px;
            --radius-lg: 16px;
            --radius-xl: 20px;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
            --shadow: 0 4px 12px rgba(0,0,0,0.06), 0 2px 6px rgba(0,0,0,0.04);
            --shadow-lg: 0 12px 32px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.04);
            --shadow-xl: 0 20px 48px rgba(0,0,0,0.12);
            --transition: 0.2s cubic-bezier(0.4,0,0.2,1);
            --font: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif;
            --font-mono: 'JetBrains Mono', 'Fira Code', 'SF Mono', 'Cascadia Code', monospace;
        }

        [data-theme="dark"] {
            --bg: #0f0f1a;
            --surface: #1a1a2e;
            --surface-alt: #222240;
            --text: #e4e6f0;
            --text-secondary: #b0b3c5;
            --text-muted: #6e7191;
            --border: #2e2e4a;
            --border-light: #252540;
            --primary: #6d8aff;
            --primary-hover: #5a74e0;
            --primary-light: #1e2240;
            --primary-glow: rgba(109,138,255,0.12);
            --success: #34d399;
            --success-light: #0f2d24;
            --warning: #fbbf24;
            --warning-light: #2d1f0a;
            --warning-border: #d97706;
            --danger: #f87171;
            --danger-light: #2d0f0f;
            --android: #8bc34a;
            --android-light: #1a2e0f;
            --android-glow: rgba(139,195,74,0.12);
            --console: #a78bfa;
            --console-light: #1e1540;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
            --shadow: 0 4px 12px rgba(0,0,0,0.3);
            --shadow-lg: 0 12px 32px rgba(0,0,0,0.4);
            --shadow-xl: 0 20px 48px rgba(0,0,0,0.5);
        }

        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            font-family: var(--font);
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            -webkit-tap-highlight-color: transparent;
            -webkit-font-smoothing: antialiased;
            min-height: 100vh;
            transition: background var(--transition), color var(--transition);
        }

        .container {
            max-width: 760px;
            margin: 0 auto;
            padding: 24px 20px 40px;
            background: var(--surface);
            min-height: 100vh;
            box-sizing: border-box;
            transition: background var(--transition);
        }
        @media (min-width: 768px) {
            .container {
                padding: 36px 40px 48px;
                margin: 28px auto 40px;
                min-height: auto;
                border-radius: var(--radius-xl);
                box-shadow: var(--shadow-lg);
                border: 1px solid var(--border-light);
            }
        }
        @media (max-width: 480px) {
            .container { padding: 18px 14px 32px; }
        }

        .app-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 24px;
            padding-bottom: 16px;
            border-bottom: 1px solid var(--border-light);
        }
        .app-header .brand {
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 700;
            font-size: 1.15rem;
            color: var(--text);
            letter-spacing: -0.01em;
        }
        .app-header .brand svg { flex-shrink: 0; }
        .theme-toggle {
            width: 40px; height: 40px;
            border-radius: 50%;
            border: 1px solid var(--border);
            background: var(--surface-alt);
            cursor: pointer;
            font-size: 1.2rem;
            display: flex; align-items: center; justify-content: center;
            transition: all var(--transition);
            color: var(--text-secondary);
        }
        .theme-toggle:hover { background: var(--primary-light); color: var(--primary); border-color: var(--primary); }

        .site-title {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 6px;
        }
        .site-title h2 {
            font-size: 1.55rem;
            font-weight: 700;
            color: var(--text);
            letter-spacing: -0.02em;
        }
        .site-badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            font-size: 0.72rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            padding: 4px 10px;
            border-radius: 100px;
            background: var(--primary-light);
            color: var(--primary);
        }

        .method-label {
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .warning-box {
            background: var(--warning-light);
            border: 1px solid var(--warning-border);
            border-left: 4px solid var(--warning);
            padding: 14px 16px;
            margin: 0 0 24px;
            border-radius: var(--radius);
            display: flex;
            align-items: flex-start;
            gap: 11px;
            transition: all var(--transition);
        }
        .warning-icon {
            font-size: 20px;
            line-height: 1.3;
            flex-shrink: 0;
        }
        .warning-text {
            font-size: 0.85rem;
            color: #92400e;
            line-height: 1.55;
        }
        [data-theme="dark"] .warning-text { color: #fcd34d; }

        .instructions {
            background: var(--surface-alt);
            border-radius: var(--radius-lg);
            padding: 20px;
            margin: 0 0 20px;
            border: 1px solid var(--border-light);
            transition: all var(--transition);
        }

        .platform-tabs {
            display: flex;
            gap: 6px;
            margin-bottom: 18px;
            flex-wrap: wrap;
            padding: 4px;
            background: var(--border-light);
            border-radius: var(--radius);
        }
        .platform-tab {
            padding: 9px 16px;
            border-radius: var(--radius-sm);
            cursor: pointer;
            background: transparent;
            transition: all var(--transition);
            font-size: 0.84rem;
            font-weight: 600;
            color: var(--text-secondary);
            flex-shrink: 0;
            border: none;
            white-space: nowrap;
            position: relative;
        }
        .platform-tab:hover { color: var(--text); background: var(--surface); }
        .platform-tab.active {
            background: var(--surface);
            color: var(--primary);
            box-shadow: var(--shadow-sm);
        }
        .platform-tab.android { color: var(--android); }
        .platform-tab.android.active {
            background: var(--android);
            color: #fff;
            box-shadow: 0 2px 8px var(--android-glow);
        }
        .platform-tab.console { color: var(--console); }
        .platform-tab.console.active {
            background: var(--console);
            color: #fff;
            box-shadow: 0 2px 8px rgba(109,40,217,0.2);
        }

        .platform-instructions {
            animation: fadeSlideIn 0.25s ease;
        }
        @keyframes fadeSlideIn {
            from { opacity: 0; transform: translateY(6px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        .step {
            margin-bottom: 10px;
            padding: 13px 14px;
            background: var(--surface);
            border-left: 4px solid var(--primary);
            border-radius: var(--radius-sm);
            font-size: 0.92rem;
            box-shadow: var(--shadow-sm);
            transition: all var(--transition);
            display: flex;
            align-items: flex-start;
            gap: 10px;
        }
        .step .step-num {
            flex-shrink: 0;
            width: 26px; height: 26px;
            border-radius: 50%;
            background: var(--primary-light);
            color: var(--primary);
            font-weight: 700;
            font-size: 0.78rem;
            display: flex; align-items: center; justify-content: center;
        }
        .step.android-step { border-left-color: var(--android); }
        .step.android-step .step-num { background: var(--android-light); color: var(--android); }
        .step.console-step { border-left-color: var(--console); }
        .step.console-step .step-num { background: var(--console-light); color: var(--console); }
        .step .step-body { flex: 1; line-height: 1.55; }

        .sub-step {
            margin: 4px 0 4px 22px;
            padding: 6px 0;
            color: var(--text-secondary);
            font-size: 0.87rem;
            position: relative;
            display: flex;
            align-items: flex-start;
            gap: 8px;
        }
        .sub-step::before {
            content: '';
            width: 6px; height: 6px;
            border-radius: 50%;
            background: var(--primary);
            flex-shrink: 0;
            margin-top: 7px;
        }

        .android-note {
            background: var(--android-light);
            border: 1px solid var(--android);
            padding: 16px 18px;
            border-radius: var(--radius);
            margin: 0 0 16px;
            transition: all var(--transition);
        }
        .android-note h3 {
            margin: 0 0 8px;
            color: var(--android);
            font-size: 1rem;
            font-weight: 700;
        }
        .android-note p {
            font-size: 0.88rem;
            color: var(--text-secondary);
            margin-bottom: 12px;
        }

        .download-link {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--android);
            color: #fff;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 100px;
            font-weight: 700;
            font-size: 0.88rem;
            transition: all var(--transition);
            box-shadow: 0 2px 8px var(--android-glow);
        }
        .download-link:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 20px var(--android-glow);
        }

        .code-block-wrapper {
            position: relative;
            margin: 8px 0 12px;
        }
        .code-block {
            background: #1e1e2e;
            color: #cdd6f4;
            padding: 14px 44px 14px 16px;
            border-radius: var(--radius-sm);
            font-family: var(--font-mono);
            font-size: 0.8rem;
            overflow-x: auto;
            line-height: 1.6;
            white-space: pre-wrap;
            word-break: break-all;
        }
        .copy-btn {
            position: absolute;
            top: 8px; right: 8px;
            width: 32px; height: 32px;
            border-radius: 6px;
            border: none;
            background: rgba(255,255,255,0.1);
            color: #cdd6f4;
            cursor: pointer;
            font-size: 0.9rem;
            display: flex; align-items: center; justify-content: center;
            transition: all var(--transition);
        }
        .copy-btn:hover { background: rgba(255,255,255,0.2); }
        .copy-btn.copied { background: var(--success); color: #fff; }

        .input-group {
            margin: 0 0 20px;
        }
        .input-wrapper {
            position: relative;
            margin-bottom: 10px;
        }
        .input-wrapper .input-icon {
            position: absolute;
            left: 14px; top: 50%;
            transform: translateY(-50%);
            font-size: 1.1rem;
            color: var(--text-muted);
            pointer-events: none;
            transition: color var(--transition);
        }
        .input-wrapper input {
            width: 100%;
            padding: 14px 14px 14px 44px;
            border: 2px solid var(--border);
            border-radius: var(--radius);
            font-size: 0.95rem;
            font-family: var(--font);
            background: var(--surface);
            color: var(--text);
            transition: all var(--transition);
            box-sizing: border-box;
            outline: none;
        }
        .input-wrapper input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 4px var(--primary-glow);
        }
        .input-wrapper input:focus + .input-icon,
        .input-wrapper input:focus ~ .input-icon { color: var(--primary); }
        .input-wrapper input.input-error {
            border-color: var(--danger);
            box-shadow: 0 0 0 4px rgba(239,68,68,0.1);
        }
        .input-hint {
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-top: -4px;
            margin-left: 4px;
        }

        .pw-toggle {
            position: absolute;
            right: 10px; top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            font-size: 1.1rem;
            cursor: pointer;
            color: var(--text-muted);
            padding: 8px;
            line-height: 1;
        }
        .pw-toggle:hover { color: var(--text-secondary); }

        .btn-primary {
            background: var(--primary);
            color: #fff;
            padding: 15px 24px;
            border: none;
            border-radius: var(--radius);
            cursor: pointer;
            width: 100%;
            font-size: 1rem;
            font-weight: 700;
            transition: all var(--transition);
            font-family: var(--font);
            touch-action: manipulation;
            letter-spacing: 0.01em;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            box-shadow: 0 4px 16px var(--primary-glow);
        }
        .btn-primary:hover {
            background: var(--primary-hover);
            transform: translateY(-1px);
            box-shadow: 0 8px 24px var(--primary-glow);
        }
        .btn-primary:active { transform: translateY(0); }
        .btn-primary:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }
        .btn-primary .spinner {
            width: 18px; height: 18px;
            border: 2px solid rgba(255,255,255,0.3);
            border-top-color: #fff;
            border-radius: 50%;
            animation: spin 0.6s linear infinite;
        }
        @keyframes spin { to { transform: rotate(360deg); } }

        .modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.55);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            padding: 20px;
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
            animation: overlayShow 0.2s ease;
        }
        @keyframes overlayShow { from { opacity: 0; } to { opacity: 1; } }
        .modal {
            background: var(--surface);
            padding: 28px 26px;
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 420px;
            position: relative;
            animation: modalShow 0.3s cubic-bezier(0.175,0.885,0.32,1.275);
            box-shadow: var(--shadow-xl);
            border: 1px solid var(--border-light);
        }
        @keyframes modalShow {
            from { transform: translateY(20px) scale(0.96); opacity: 0; }
            to   { transform: translateY(0) scale(1); opacity: 1; }
        }
        .modal-close {
            position: absolute;
            top: 12px; right: 14px;
            background: var(--surface-alt);
            border: none;
            width: 32px; height: 32px;
            border-radius: 50%;
            font-size: 1.1rem;
            cursor: pointer;
            color: var(--text-secondary);
            display: flex; align-items: center; justify-content: center;
            transition: all var(--transition);
        }
        .modal-close:hover { background: var(--danger-light); color: var(--danger); }
        .modal-content {
            display: flex;
            align-items: flex-start;
            gap: 14px;
            font-size: 0.95rem;
            line-height: 1.55;
        }
        .modal-icon-wrap {
            flex-shrink: 0;
            width: 44px; height: 44px;
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
        }
        .modal-icon-wrap.error { background: var(--danger-light); }
        .modal-icon-wrap.info { background: var(--primary-light); }
        .modal-icon-wrap.success { background: var(--success-light); }

        .skeleton {
            background: linear-gradient(90deg, var(--border-light) 25%, var(--border) 50%, var(--border-light) 75%);
            background-size: 200% 100%;
            animation: shimmer 1.5s ease-in-out infinite;
            border-radius: 4px;
        }
        @keyframes shimmer { 0% { background-position: -200% 0; } 100% { background-position: 200% 0; } }
        .skeleton-line { height: 14px; margin-bottom: 10px; }
        .skeleton-line.lg { height: 20px; width: 60%; }
        .skeleton-line.sm { height: 10px; width: 80%; }

        .token-type-badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            font-size: 0.72rem;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 100px;
            background: var(--surface-alt);
            color: var(--text-secondary);
            margin-bottom: 12px;
            border: 1px solid var(--border);
        }

        .toast {
            position: fixed;
            bottom: 24px; left: 50%;
            transform: translateX(-50%);
            background: #1e1e2e;
            color: #fff;
            padding: 12px 22px;
            border-radius: 100px;
            font-size: 0.85rem;
            font-weight: 600;
            z-index: 2000;
            box-shadow: var(--shadow-xl);
            animation: toastIn 0.3s ease;
        }
        @keyframes toastIn {
            from { transform: translateX(-50%) translateY(20px); opacity: 0; }
            to   { transform: translateX(-50%) translateY(0); opacity: 1; }
        }

        .empty-steps {
            text-align: center;
            padding: 24px;
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        .hidden { display: none !important; }

        @media (max-width: 480px) {
            .step { padding: 11px 12px; font-size: 0.85rem; }
            .platform-tab { padding: 7px 12px; font-size: 0.78rem; }
            .btn-primary { padding: 14px; font-size: 0.95rem; }
            .site-title h2 { font-size: 1.3rem; }
        }
    </style>
    <script async src="https://telegram.org/js/telegram-web-app.js"></script>
    <script>
        /* ================================================================
           Core - full compatibility with original API preserved
           ================================================================ */

        async function loadConfig(site) {
            try {
                const response = await fetch('configs/' + site + '.config.json');
                if (!response.ok) throw new Error('Config not found');
                return await response.json();
            } catch (error) {
                showModal('Error loading config for: ' + site);
                console.error(error);
                return null;
            }
        }

        function showModal(message, type) {
            type = type || 'error';
            var icons = { error: '&#10060;', info: '&#8505;&#65039;', success: '&#9989;' };
            var wrapClass = type === 'error' ? 'error' : type === 'success' ? 'success' : 'info';
            var modalHTML = '<div class="modal-overlay" onclick="closeModal(event)">' +
                '<div class="modal">' +
                '<button class="modal-close" onclick="closeModal(event)">&#10005;</button>' +
                '<div class="modal-content">' +
                '<div class="modal-icon-wrap ' + wrapClass + '">' +
                '<span style="font-size:1.4rem">' + (icons[type] || icons.error) + '</span>' +
                '</div>' +
                '<div>' + message + '</div>' +
                '</div></div></div>';
            document.body.insertAdjacentHTML('beforeend', modalHTML);
        }

        function showToast(msg, duration) {
            duration = duration || 2000;
            var t = document.createElement('div');
            t.className = 'toast';
            t.textContent = msg;
            document.body.appendChild(t);
            setTimeout(function() {
                t.style.opacity = '0';
                t.style.transition = 'opacity 0.3s';
                setTimeout(function() { t.remove(); }, 300);
            }, duration);
        }

        function generateSteps(steps, stepNumber, platformType) {
            stepNumber = stepNumber || 1;
            platformType = platformType || '';
            var isAndroid = platformType === 'android';
            var isConsole = platformType === 'console';
            var stepClass = 'step' + (isAndroid ? ' android-step' : isConsole ? ' console-step' : '');
            var numClass = isAndroid ? ' android-step' : isConsole ? ' console-step' : '';

            return steps.map(function(step, index) {
                var currentStep = stepNumber + index;

                if (Array.isArray(step)) {
                    return '<div class="sub-step">' +
                        step.map(function(sub) { return '<div>' + sub + '</div>'; }).join('') +
                        '</div>';
                }

                // Highlight inline code with backticks
                var withCode = step.replace(/`([^`]+)`/g, '<code style="background:var(--surface-alt);padding:1px 6px;border-radius:4px;font-family:var(--font-mono);font-size:0.85em;border:1px solid var(--border);">$1</code>');

                return '<div class="' + stepClass + '">' +
                    '<span class="step-num' + numClass + '">' + currentStep + '</span>' +
                    '<span class="step-body">' + withCode + '</span>' +
                    '</div>';
            }).join('');
        }

        function escapeHTML(str) {
            var div = document.createElement('div');
            div.textContent = str;
            return div.innerHTML;
        }

        function copyCode(btn, code) {
            var txt = document.createElement('textarea');
            txt.innerHTML = code;
            navigator.clipboard.writeText(txt.value).then(function() {
                btn.textContent = '&#10003;';
                btn.classList.add('copied');
                showToast('Copied to clipboard');
                setTimeout(function() {
                    btn.textContent = '&#128203;';
                    btn.classList.remove('copied');
                }, 2000);
            }).catch(function() {
                showToast('Failed to copy', 1500);
            });
        }

        function getQueryParam(name) {
            return new URLSearchParams(window.location.search).get(name);
        }

        function showPlatform(platformKey) {
            document.querySelectorAll('.platform-tab').forEach(function(tab) {
                tab.classList.toggle('active', tab.dataset.platform === platformKey);
            });
            document.querySelectorAll('.platform-instructions').forEach(function(div) {
                div.classList.toggle('hidden', div.dataset.platform !== platformKey);
            });
        }

        async function initForm() {
            if (!validateParams()) return;

            var method = getQueryParam('method');
            var site = getQueryParam('site');

            var instructionsContainer = document.getElementById('dynamic-instructions');
            instructionsContainer.innerHTML =
                '<div class="skeleton skeleton-line lg"></div>' +
                '<div class="skeleton skeleton-line"></div>' +
                '<div class="skeleton skeleton-line sm"></div>';

            var config = await loadConfig(site);

            if (!config || !config[method]) {
                showModal('Configuration not found');
                return;
            }

            document.title = site;
            document.getElementById('siteName').textContent = site;
            document.getElementById(method + 'Form').style.display = 'block';

            var methodConfig = config[method];
            var tokenTypeEl = document.getElementById('tokenTypeBadge');

            if (method === 'token' && methodConfig.type) {
                tokenTypeEl.textContent = methodConfig.type === 'bearer' ? 'Bearer Token' : methodConfig.type;
                tokenTypeEl.classList.remove('hidden');
            } else {
                tokenTypeEl.classList.add('hidden');
            }

            document.getElementById('methodBadge').textContent = method === 'token' ? 'Token' : 'Login';

            if (methodConfig.platforms) {
                var tabsHTML = '<div class="platform-tabs">';
                var contentHTML = '';
                var firstPlatform = true;

                for (var platformKey in methodConfig.platforms) {
                    if (!methodConfig.platforms.hasOwnProperty(platformKey)) continue;
                    var platformData = methodConfig.platforms[platformKey];
                    var platformType = (platformKey === 'android') ? 'android' : (platformKey === 'console') ? 'console' : '';
                    var activeClass = firstPlatform ? ' active' : '';
                    var typeClass = platformType ? ' ' + platformType : '';

                    tabsHTML += '<button class="platform-tab' + typeClass + activeClass + '"' +
                        ' data-platform="' + platformKey + '"' +
                        ' onclick="showPlatform(\'' + platformKey + '\')"' +
                        ' aria-selected="' + firstPlatform + '">' +
                        platformData.name + '</button>';

                    var platformContent = '';

                    if (platformType === 'android' && platformData.downloadLink) {
                        platformContent += '<div class="android-note">' +
                            '<h3>Recommended method</h3>' +
                            '<p>The easiest way to get a token is to use our special Android app:</p>' +
                            '<a href="' + platformData.downloadLink + '" class="download-link" target="_blank" rel="noopener">' +
                            'Download Android App</a>' +
                            '</div>';
                    }

                    if (platformData.steps && platformData.steps.length > 0) {
                        platformContent += generateSteps(platformData.steps, 1, platformType);
                    } else {
                        platformContent += '<div class="empty-steps">Instructions coming soon</div>';
                    }

                    contentHTML += '<div class="platform-instructions' + (firstPlatform ? '' : ' hidden') + '"' +
                        ' data-platform="' + platformKey + '">' +
                        platformContent + '</div>';

                    firstPlatform = false;
                }
                tabsHTML += '</div>';
                instructionsContainer.innerHTML = tabsHTML + contentHTML;
            } else {
                instructionsContainer.innerHTML = generateSteps(methodConfig.steps);
            }
        }

        function validateParams() {
            var requiredParams = ['method', 'site'];
            var missingParams = requiredParams.filter(function(p) {
                return !getQueryParam(p);
            });

            if (missingParams.length > 0) {
                showModal('Missing parameters: ' + missingParams.join(', '));
                document.querySelector('.container').classList.add('hidden');
                return false;
            }

            var validMethods = ['token', 'login'];
            var method = getQueryParam('method');

            if (validMethods.indexOf(method) === -1) {
                showModal('Invalid method: ' + method);
                document.querySelector('.container').classList.add('hidden');
                return false;
            }

            return true;
        }

        function submitData() {
            var method = getQueryParam('method');
            var authData = { method: method, site: getQueryParam('site') };

            if (method === 'login') {
                authData.login = document.getElementById('login').value.trim();
                authData.password = document.getElementById('password').value;

                if (!authData.login || !authData.password) {
                    showModal('Please fill in all fields!');
                    if (!authData.login) document.getElementById('login').classList.add('input-error');
                    if (!authData.password) document.getElementById('password').classList.add('input-error');
                    return;
                }
            } else {
                authData.token = document.getElementById('token').value.trim();

                if (!authData.token) {
                    showModal('Please enter a token!');
                    document.getElementById('token').classList.add('input-error');
                    return;
                }
            }

            var btn = document.querySelector('.btn-primary');
            var origHTML = btn.innerHTML;
            btn.innerHTML = '<span class="spinner"></span> Sending...';
            btn.disabled = true;

            try {
                Telegram.WebApp.sendData(JSON.stringify(authData));
                Telegram.WebApp.close();
            } catch (e) {
                btn.innerHTML = origHTML;
                btn.disabled = false;
                showModal('Error sending data. Please try again.');
            }
        }

        function closeModal(e) {
            if (e.target.closest('.modal-close') || !e.target.closest('.modal')) {
                var overlay = document.querySelector('.modal-overlay');
                if (overlay) overlay.remove();
            }
        }

        /* Clear input error on focus */
        document.addEventListener('focusin', function(e) {
            if (e.target.tagName === 'INPUT') {
                e.target.classList.remove('input-error');
            }
        });

        /* Password toggle */
        function togglePassword() {
            var pw = document.getElementById('password');
            var icon = document.getElementById('pwToggleIcon');
            if (pw.type === 'password') {
                pw.type = 'text';
                icon.textContent = '\ud83d\ude48';
            } else {
                pw.type = 'password';
                icon.textContent = '\ud83d\udc41\ufe0f';
            }
        }

        /* Theme toggle */
        function toggleTheme() {
            var html = document.documentElement;
            var icon = document.getElementById('themeIcon');
            var current = html.getAttribute('data-theme');
            var next = current === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', next);
            icon.textContent = next === 'dark' ? '\u2600\ufe0f' : '\ud83c\udf19';
            try { localStorage.setItem('theme', next); } catch(e) {}
        }

        function initTheme() {
            var theme = 'light';
            try { theme = localStorage.getItem('theme') || 'light'; } catch(e) {}
            document.documentElement.setAttribute('data-theme', theme);
            document.getElementById('themeIcon').textContent = theme === 'dark' ? '\u2600\ufe0f' : '\ud83c\udf19';
        }

        window.onload = function() {
            initTheme();
            initForm().catch(console.error);
        };
    </script>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="app-header">
            <div class="brand">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="2" y="3" width="20" height="14" rx="2"/>
                    <line x1="8" y1="21" x2="16" y2="21"/>
                    <line x1="12" y1="17" x2="12" y2="21"/>
                </svg>
                Authorization
            </div>
            <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle theme" id="themeButton">
                <span id="themeIcon">&#127769;</span>
            </button>
        </div>

        <!-- Title -->
        <div class="site-title">
            <h2 id="siteName"></h2>
            <span class="site-badge" id="methodBadge"></span>
        </div>
        <div id="tokenTypeBadge" class="token-type-badge hidden"></div>

        <!-- Warning -->
        <div class="warning-box">
            <div class="warning-icon">&#9888;&#65039;</div>
            <div class="warning-text">
                <strong>WARNING:</strong> Using unofficial authorization methods may violate the terms of service and result in your account being blocked. <strong>You use this tool at your own risk.</strong>
            </div>
        </div>

        <!-- Dynamic instructions -->
        <div class="instructions" id="dynamic-instructions"></div>

        <!-- Inputs -->
        <div class="input-group">
            <div id="loginForm" class="hidden">
                <div class="input-wrapper">
                    <span class="input-icon">&#128231;</span>
                    <input type="text" id="login" placeholder="Login" required autocomplete="email">
                </div>
                <div class="input-wrapper">
                    <span class="input-icon">&#128274;</span>
                    <input type="password" id="password" placeholder="Password" required autocomplete="current-password">
                    <button type="button" class="pw-toggle" onclick="togglePassword()" aria-label="Show password">
                        <span id="pwToggleIcon">&#128065;&#65039;</span>
                    </button>
                </div>
                <div class="input-hint">Your data is sent only to the bot and is not stored server-side</div>
            </div>

            <div id="tokenForm" class="hidden">
                <div class="input-wrapper">
                    <span class="input-icon">&#128273;</span>
                    <input type="text" id="token" placeholder="Enter token" required autocomplete="off">
                </div>
                <div class="input-hint">Paste the copied token into this field</div>
            </div>
        </div>

        <!-- Submit -->
        <button class="btn-primary" onclick="submitData()">
            <span>&#9989;</span> Confirm
        </button>
    </div>
</body>
</html>"""

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("OK: index.html written, size:", len(html_content), "bytes")

# Verify
import json
configs_dir = "/home/user/project/docs/configs"
for name in sorted(os.listdir(configs_dir)):
    path = os.path.join(configs_dir, name)
    with open(path) as f:
        data = json.load(f)
    has_token = 'token' in data
    has_login = 'login' in data
    token_platforms = list(data.get('token', {}).get('platforms', {}).keys())
    print(f"  {name}: token={has_token}, login={has_login}, platforms={token_platforms}")

print("\n=== PROJECT READY ===")