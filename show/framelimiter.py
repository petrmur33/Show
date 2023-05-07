import logging
import time

log = logging.getLogger(__name__)

class FrameLimiter():
    def __init__(self, limit: int | str) -> None:
        self.vsync = True if limit == "vsync" else False
        self.limit = limit
        self.old = time.time()
        self.elapsed = 0
        self.frames = 0

    def tick(self) -> float:
        # calculate deltatime
        now = time.time()
        dt = now - self.old

        # sleep to reach frame rate limit
        if not self.vsync:
            time.sleep(max(1 / self.limit - dt, 0))

        # calculate deltatime
        now = time.time()
        dt = now - self.old
        self.old = now

        self.elapsed += dt
        self.frames += 1

        # debugging message every second
        if self.elapsed >= 1:
            log.debug(self.frames)
            self.elapsed = 0
            self.frames = 0

        if not self.vsync:
            return max(1 / self.limit, dt)
        return dt
