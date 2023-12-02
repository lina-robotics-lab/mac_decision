# Python MultiProcessing Package

Code from Toyota Exp,
```python
receive_index = mp.Value('d', 0.0)
    lock = mp.Lock()
    procs = [Process(target=subscriber_gps_agent, args=(shared_list, receive_index, lock)),
             Process(target=subscriber_can_agent, args=(shared_list, receive_index, lock))]

    if args.if_radar:
        procs.append(Process(target=subscriber_radar_agent, args=(shared_list, lock)))
    else:
        procs.append(Process(target=traffic, args=(shared_list, lock, args.task, args.case, args.surr_flag)))
    procs.append(Process(target=controller_agent, args=(shared_list, receive_index, args.if_save, args.if_radar, lock,
                                                        args.task, args.case, args.noise_factor, args.load_dir,
                                                        args.load_ite, args.result_dir, args.model_only_test, args.clipped_v)))
    procs.append(Process(target=plot_agent, args=(shared_list, lock, args.task, args.model_only_test)))

    for p in procs:
        p.start()
    for p in procs:
        p.join()
```

## Use Lock
```python
with lock:
    % EDIT shared_list
```