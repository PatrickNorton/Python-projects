(defmacro strings (&rest args)
  `(quote ,(loop for x in args
                 collect (coerce (string x) 'list))))

(defparameter dictionary (strings apple banana orange))

(defparameter guesses nil)

(defparameter word nil)

(defparameter guesses nil)

(defun wrong-guesses ()
  (remove-if (lambda (c) (find c word)) guesses))

(defun won? ()
  (every (lambda (c) (find c guesses)) word))

(defun lost? ()
  (> (length wrong-guesses) 10))

(defun format-word (word)
  (format nil "~{~a~^ ~}"
           word))

(defun set-word
    (setq word (nth (random (length dictionary)) dictionary)))

(defun hangman ()
  (let 'exit-hangman nil)
  (loop until (= exit-hangman t)
        do (hangman-game))
  (princ "Play again? (y/n) ")
  (let exit-hangman (= (read) "y"))
  (fresh-line))

(defun hangman-game ()
  (set-word)
  (loop until (or (won?) (lost?))
        do (turn))
  (if (won?)
      (princ "You won!")
    (princ "You lost.")))

(defun turn ()
  (princ "Enter a letter: ")
  (let 'entered (read))
  (if entered (pushnew (char-lowcase entered) guesses))
  )