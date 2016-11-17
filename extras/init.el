(package-initialize)
;; M-x package-list-packages
(setq user-full-name "Miguel Piña"
      user-mail-address "miguel_pinia@ciencias.unam.mx"
      package-archives '(("marmalade" . "http://marmalade-repo.org/packages/")
                         ("tromey" . "http://tromey.com/elpa/")
                         ("melpa-stable" . "https://stable.melpa.org/packages/")
                         ("melpa" . "https://melpa.org/packages/")
                         ("org" . "http://orgmode.org/elpa/")
                         ("gnu" . "https://elpa.gnu.org/packages/")))
;; M-x package-list-packages
(load-theme 'wombat t)
(set-frame-font "hack 14")
(global-hl-line-mode 1)
(blink-cursor-mode 0);; Cursor estático
(show-paren-mode 1)
(linum-mode 1)
(setq-default auto-save-default nil ;; Evitar generar archivos de la forma #archivo#
              save-place t ;; Guarda la línea en que estabas cuando cierras el archivo
              create-lockfiles nil ;; Evita crear candados para la edición de archivos
              inhibit-startup-message t ;; Evita el mensaje de emacs.
              indent-tabs-mode nil ;; Evita ingresar tabs "duros"
              tab-width 4 ;; Tamaño de espacios para un tabulador
              x-select-enable-clipboard t
              x-select-enable-primary t
              save-interprogram-paste-before-kill t
              apropos-do-all t
              mouse-yank-at-point t)
(global-set-key (kbd "C-s") 'isearch-forward-regexp)
(global-set-key (kbd "C-r") 'isearch-backward-regexp)
(global-set-key (kbd "C-M-s") 'isearch-forward)
(global-set-key (kbd "C-M-r") 'isearch-backward)
(defun trailing-whitespaces ()
    "Muestra los espacios en blanco al final de cada linea."
    (interactive)
    (setq show-trailing-whitespace t))
(add-hook 'prog-mode-hook 'trailing-whitespaces)
(add-hook 'LaTeX-mode-hook 'trailing-whitespaces)
(add-hook 'prog-mode-hook  (lambda ()
                             (add-to-list 'write-file-functions
                                          'delete-trailing-whitespace)));; Eliminar espacios en blanco después de un último caracter
(add-hook 'LaTeX-mode-hook (lambda () (add-to-list 'write-file-functions 'delete-trailing-whitespace)))

(require 'helm-config)
(require 'helm)

(helm-mode 1)
(global-set-key (kbd "C-c h") 'helm-command-prefix)
(global-set-key (kbd "M-x") 'helm-M-x)
(global-set-key (kbd "C-x C-f") 'helm-find-files)
(define-key helm-map (kbd "C-i") 'helm-execute-persistent-action)
(define-key helm-map (kbd "C-z")  'helm-select-action)
(define-key helm-map (kbd "<tab>") 'helm-execute-persistent-action)
(global-set-key (kbd "C-x b") 'helm-mini)

;; neotree
(require 'neotree)
(global-set-key [f8] 'neotree-toggle)
(setq neo-smart-open t)

;; yasnippet
(require 'yasnippet)
(yas-global-mode 1)

;; auto-complete
(require 'auto-complete)
(set-default 'ac-sources
             '(ac-source-abbrev
               ac-source-dictionary
               ;; ac-source-yasnippet
               ac-source-words-in-buffer
               ac-source-words-in-same-mode-buffers
               ;; ac-source-semantic
               ))
(global-auto-complete-mode t)
(setq-default ac-auto-start 0.5
              ac-use-overriding-local-map nil
              ac-use-menu-map t
              ac-candidate-limit 20
              ac-ignore-case nil)

(require 'nyan-mode)
(nyan-mode t)
(nyan-start-animation)
(setq nyan-wavy-trail t)
