(defun ack (m n)
  (cond ((zerop m) (1+ n))
        ((zerop n) (ack (1- m) 1))
        (t (ack (1- m) (ack m (1- n))))))

(princ (ack 0 2))
